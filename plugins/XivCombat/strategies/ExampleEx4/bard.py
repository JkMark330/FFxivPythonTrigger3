from math import radians
from time import perf_counter

from XivCombat.utils import a, s
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Rectangle, Sector, select, FarCircle


def cnt_enemy(data: 'LogicData', ability):
    target, cnt = select(data, data.valid_enemies, ability)
    if not cnt: return data.target, 0
    if data.config['single'] == define.FORCE_SINGLE: return data.target, 1
    if data.config['single'] == define.FORCE_MULTI: return data.target, 3
    return target, cnt


def res_lv(data: 'LogicData'):
    match data.config['resource']:
        case define.RESOURCE_SQUAND:
            return 2
        case define.RESOURCE_NORMAL:
            return 1
        case define.RESOURCE_STINGY:
            return 0
        case _:
            return int(data.max_ttk > 10)


quick_nock = Sector(12, radians(90))
apex_arrow = Rectangle(25, 2)
shadow_bite = FarCircle(25, 5)
rain_of_death = FarCircle(25, 8)


class BardLogic(Strategy):
    name = "ny/bard_logic"
    job = "Bard"

    def __init__(self):
        self.last_song = 0

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        match action_id:
            case a('大地神的抒情恋歌') | a('光阴神的礼赞凯歌'):
                mo_entity = api.get_mo_target()
                if mo_entity and api.action_type_check(action_id, mo_entity):
                    return UseAbility(action_id, mo_entity.id)

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST)
            if data.actor_distance_effective(single_target) > 25: return

        res = res_lv(data)
        if res and (res > 1 or data.gauge.soul_gauge >= 80 and data[a('猛者强击')] > 10):
            apex_arrow_target, apex_arrow_cnt = cnt_enemy(data, apex_arrow)
            if apex_arrow_cnt: return UseAbility(a('绝峰箭'), apex_arrow_target.id)

        if s('Shadowbite Ready') in data.effects:
            shadow_bite_target, shadow_bite_cnt = select(data, data.valid_enemies, shadow_bite)
        else:
            shadow_bite_target, shadow_bite_cnt = single_target, 0
        if s('直线射击预备') in data.effects:
            if shadow_bite_cnt < 4:
                return UseAbility(a('直线射击'), single_target.id)
            else:
                return UseAbility(a('影噬箭'), shadow_bite_target.id)
        if shadow_bite_cnt > 2:
            return UseAbility(a('影噬箭'), shadow_bite_target.id)

        if res and s('Blast Arrow Ready') in data.effects and (res > 1 or data.effects[s('Blast Arrow Ready')].timer >= 80 > data[a('猛者强击')] + 3):
            apex_arrow_target, apex_arrow_cnt = cnt_enemy(data, apex_arrow)
            if apex_arrow_cnt: return UseAbility(a('Blast Arrow'), apex_arrow_target.id)

        if data.me.level >= 18:
            quick_nock_target, quick_nock_cnt = cnt_enemy(data, quick_nock)
            if quick_nock_cnt > (2 if data.me.level < 82 else 1):
                return UseAbility(a('连珠箭'), quick_nock_target.id)

        if data.me.level >= 6:
            dot_targets = [e for e in data.valid_enemies if data.ttk(e) > 20 and data.actor_distance_effective(e) <= 25]
            if dot_targets:
                dot_targets.sort(key=lambda e: data.ttk(e), reverse=True)
                if data.me.level >= 64:
                    wind_dot = s('狂风蚀箭')
                    poison_dot = s('烈毒咬箭')
                else:
                    wind_dot = s('风蚀箭')
                    poison_dot = s('毒咬箭')
                dot_re_cast_time = 10 if 0 < data.effect_time(s('猛者强击')) < 6 else 3
                for target in dot_targets:
                    t_effect = target.effects.get_dict(source=data.me.id)
                    wind_remain = getattr(t_effect.get(wind_dot), 'timer', 0)
                    poison_remain = getattr(t_effect.get(poison_dot), 'timer', 0)
                    if data.skill_unlocked(a('伶牙俐齿')) and 0 < min(wind_remain, poison_remain) < dot_re_cast_time + 3:
                        return UseAbility(a('伶牙俐齿'), target.id)
                    elif data.skill_unlocked(a('风蚀箭')) and wind_remain < dot_re_cast_time:
                        return UseAbility(a('风蚀箭'), target.id)
                    elif poison_remain < dot_re_cast_time:
                        return UseAbility(a('毒咬箭'), target.id)

        if shadow_bite_cnt > 1:
            return UseAbility(a('影噬箭'), shadow_bite_target.id)
        return UseAbility(a('强力射击'), single_target.id)

    def use_song(self, song_id, target_id):
        self.last_song = perf_counter()
        return UseAbility(song_id, target_id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST)
            if data.actor_distance_effective(single_target) > 25: return

        song = data.gauge.song_type.value
        blood_letter = data[a('失血箭')]
        if data.me.level < 84: blood_letter -= 15
        can_use_blood_letter = blood_letter < 15
        if data.skill_unlocked(a('死亡箭雨')):
            rain_of_death_target, rain_of_death_cnt = cnt_enemy(data, rain_of_death)
        else:
            rain_of_death_target, rain_of_death_cnt = single_target, 0
        data.plugin.logger(f'song: {song}, {data[a("失血箭")]:.2f},{blood_letter:.2f}')
        if can_use_blood_letter and blood_letter < (10 if song == 'ballad' else 3):
            if rain_of_death_cnt > 1:
                return UseAbility(a('死亡箭雨'), rain_of_death_target.id)
            else:
                return UseAbility(a('失血箭'), single_target.id)
        res = res_lv(data)
        if not res: return

        if song == 'minuet' and data.gauge.song_procs > 2:
            return UseAbility(a('完美音调'), single_target.id)

        minuet = data[a('放浪神的小步舞曲')]
        ballad = data[a('贤者的叙事谣')]
        if self.last_song < perf_counter() - 2:
            if not song or (song == 'paeon' and max(minuet, ballad) <= 45):
                if rain_of_death_cnt > 2:
                    if not ballad: return self.use_song(a('贤者的叙事谣'), single_target.id)
                    if not minuet: return self.use_song(a('放浪神的小步舞曲'), single_target.id)
                else:
                    if not minuet: return self.use_song(a('放浪神的小步舞曲'), single_target.id)
                    if not ballad: return self.use_song(a('贤者的叙事谣'), single_target.id)
                if not data[a('军神的赞美歌')]: return self.use_song(a('军神的赞美歌'), single_target.id)

        if data.me.level < 4: return
        raging_strikes = data[a('猛者强击')]
        if not raging_strikes and (song or not data.skill_unlocked(a('贤者的叙事谣'))):
            other_cds = []
            if data.skill_unlocked(a('纷乱箭')): other_cds.append(data[a('纷乱箭')])
            if data.skill_unlocked(a('战斗之声')): other_cds.append(data[a('战斗之声')])
            if data.skill_unlocked(a('Radiant Finale')): other_cds.append(data[a('Radiant Finale')])
            if not other_cds or max(other_cds) < 10: return UseAbility(a('猛者强击'), data.me.id)
        if raging_strikes > 100:
            if not data[a('战斗之声')]:
                return UseAbility(a('战斗之声'), data.me.id)
            if not data[a('Radiant Finale')]:
                return UseAbility(a('Radiant Finale'), data.me.id)
            if not data[a('纷乱箭')] and s('直线射击预备') not in data.effects:
                return UseAbility(a('纷乱箭'), data.me.id)
            if can_use_blood_letter:
                if rain_of_death_cnt > 1:
                    return UseAbility(a('死亡箭雨'), rain_of_death_target.id)
                else:
                    return UseAbility(a('失血箭'), single_target.id)

        if not data[a('侧风诱导箭')] and raging_strikes > 40:
            return UseAbility(a('侧风诱导箭'), single_target.id)
        if not data[a('九天连箭')] and song:
            match song:
                case 'minuet':
                    if data.gauge.song_procs > 2:
                        return UseAbility(a('完美音调'), single_target.id)
                case 'ballad':
                    if blood_letter < 10:
                        return UseAbility(a('失血箭'), single_target.id)
                case 'paeon':
                    if data.gauge.song_procs >= 4 and min(data.gauge.song_milliseconds, max(minuet, ballad) - 45) < 30:
                        return
            return UseAbility(a('九天连箭'), single_target.id)