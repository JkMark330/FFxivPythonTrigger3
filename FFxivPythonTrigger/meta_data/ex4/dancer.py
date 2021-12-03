from ..base import *


class Actions:

    class Cascade(ActionBase):
        """
Delivers an attack with a potency of 180.
Additional Effect: 50% chance of granting Flourishing Symmetry
Duration: 30s
※Action changes to Emboite while dancing.
        """
        id = 15989
        name = {'Cascade', '瀑泻'}

    class Fountain(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Cascade
Combo Potency: 240
Combo Bonus: 50% chance of granting Flourishing Flow
Duration: 30s
※Action changes to Entrechat while dancing.
        """
        id = 15990
        name = {'Fountain', '喷泉'}
        combo_action = 15989

    class Windmill(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Additional Effect: 50% chance of granting Flourishing Symmetry
Duration: 30s
※Action changes to Emboite while dancing.
        """
        id = 15993
        name = {'Windmill', '风车'}

    class StandardStep(ActionBase):
        """
Begin dancing, granting yourself Standard Step.
Duration: 15s
Action changes to Standard Finish while dancing.
Only Standard Finish, En Avant, step actions, role actions, Sprint, and Limit Break can be performed while dancing.
Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
>> 1818, Standard Step, Caught up in the dance and only able to execute step actions, role actions, Sprint, Limit Break, Standard Finish, and En Avant.
>> 2023, Standard Step, Caught up in the dance and only able to execute step actions, additional actions, Head Graze, Bolt, Medical Kit, Standard Finish, and En Avant.
        """
        id = 15997
        name = {'Standard Step', '标准舞步'}

    class Emboite(ActionBase):
        """
Perform an emboite.
When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
        """
        id = 15999
        name = {'蔷薇曲脚步', 'Emboite'}

    class Entrechat(ActionBase):
        """
Perform an entrechat.
When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
        """
        id = 16000
        name = {'小鸟交叠跳', 'Entrechat'}

    class Jete(ActionBase):
        """
Perform a jete.
When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
        """
        id = 16001
        name = {'绿叶小踢腿', 'Jete'}

    class Pirouette(ActionBase):
        """
Perform a pirouette.
When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
        """
        id = 16002
        name = {'金冠趾尖转', 'Pirouette'}

    class StandardFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 360
1 Step: 540
2 Steps: 720
(source.job==38?(source.level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner)
Damage bonus of Standard Finish varies with number of successful steps.
1 Step: 2%
2 Steps: 5%
Duration: 60s
Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
>> 2113, Standard Finish, Weaponskill and spell cast and recast time are reduced.
>> 2024, Standard Finish, Weaponskill and spell cast and recast time are reduced.
>> 2105, Standard Finish, Damage dealt is increased.
>> 1821, Standard Finish, Damage dealt is increased.
        """
        id = 16003
        name = {'标准舞步结束', 'Standard Finish'}

    class SingleStandardFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 360
1 Step: 540
2 Steps: 720
(source.job==38?(source.level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner)
Damage bonus of Standard Finish varies with number of successful steps.
1 Step: 2%
2 Steps: 5%
Duration: 60s
Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
        """
        id = 16191
        name = {'单色标准舞步结束', 'Single Standard Finish'}

    class DoubleStandardFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 360
1 Step: 540
2 Steps: 720
(source.job==38?(source.level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner)
Damage bonus of Standard Finish varies with number of successful steps.
1 Step: 2%
2 Steps: 5%
Duration: 60s
Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
        """
        id = 16192
        name = {'Double Standard Finish', '双色标准舞步结束'}

    class ReverseCascade(ActionBase):
        """
Delivers an attack with a potency of 240.
(source.job==38?(source.level>=30?Additional Effect: 50% chance of granting a Fourfold Feather
:):)Can only be executed while under the effect of Flourishing Symmetry.
※Action changes to Jete while dancing.
        """
        id = 15991
        name = {'逆瀑泻', 'Reverse Cascade'}

    class Bladeshower(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Combo Action: Windmill
Combo Potency: 140
Combo Bonus: 50% chance of granting Flourishing Flow
Duration: 30s
※Action changes to Entrechat while dancing.
        """
        id = 15994
        name = {'落刃雨', 'Bladeshower'}
        combo_action = 15993

    class FanDance(ActionBase):
        """
Delivers an attack with a potency of 150.
Additional Effect: 50% chance of granting Threefold Fan Dance
Duration: 30s
Can only be executed while in possession of Fourfold Feathers.
        """
        id = 16007
        name = {'扇舞·序', 'Fan Dance'}

    class RisingWindmill(ActionBase):
        """
Delivers an attack with a potency of 140 to all nearby enemies.
Additional Effect: 50% chance of granting a Fourfold Feather
Can only be executed while under the effect of Flourishing Symmetry.
※Action changes to Jete while dancing.
        """
        id = 15995
        name = {'Rising Windmill', '升风车'}

    class Fountainfall(ActionBase):
        """
Delivers an attack with a potency of 300.
Additional Effect: 50% chance of granting a Fourfold Feather
Can only be executed while under the effect of Flourishing Flow.
※Action changes to Pirouette while dancing.
        """
        id = 15992
        name = {'Fountainfall', '坠喷泉'}

    class Bloodshower(ActionBase):
        """
Delivers an attack with a potency of 180 to all nearby enemies.
Additional Effect: 50% chance of granting a Fourfold Feather
Can only be executed while under the effect of Flourishing Flow.
※Action changes to Pirouette while dancing.
        """
        id = 15996
        name = {'Bloodshower', '落血雨'}

    class FanDanceIi(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Additional Effect: 50% chance of granting Threefold Fan Dance
Duration: 30s
Can only be executed while in possession of Fourfold Feathers.
        """
        id = 16008
        name = {'扇舞·破', 'Fan Dance II'}

    class EnAvant(ActionBase):
        """
Quickly dash 10 yalms forward.
(source.job==38?(source.level>=68?Maximum Charges: (source.job==38?(source.level>=78?3:2):2)
:):)Cannot be executed while bound.
>> 2048, En Avant, Cascade is upgraded to Reverse Cascade, Fountain is upgraded to Fountainfall, Windmill is upgraded to Rising Windmill, and Bladeshower is upgraded to Bloodshower.
        """
        id = 16010
        name = {'En Avant', '前冲步'}

    class CuringWaltz(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 300
Additional Effect: Party member designated as your Dance Partner will also heal self and nearby party members
        """
        id = 16015
        name = {'治疗之华尔兹', 'Curing Waltz'}

    class ShieldSamba(ActionBase):
        """
Reduces damage taken by self and nearby party members by 10%.
Duration: 15s
Effect cannot be stacked with bard's Troubadour or machinist's Tactician.
>> 1826, Shield Samba, Damage taken is reduced.
        """
        id = 16012
        name = {'Shield Samba', '防守之桑巴'}

    class ClosedPosition(ActionBase):
        """
Grants you Closed Position and designates a party member as your Dance Partner, allowing you to share the effects of Standard Finish, Curing Waltz, Devilment, and Tillana with said party member.
Effect ends upon reuse.
>> 2026, Closed Position, Sharing the effects of certain actions with target party member.
>> 1823, Closed Position, Sharing the effects of certain actions with target party member.
        """
        id = 16006
        name = {'闭式舞姿', 'Closed Position'}

    class Ending(ActionBase):
        """
Ends dance with your partner.
        """
        id = 18073
        name = {'解除闭式舞姿', 'Ending'}

    class Devilment(ActionBase):
        """
Increases critical hit rate and direct hit rate by 20%.
Duration: 20s
Additional Effect: Party member designated as your Dance Partner will also receive the effect of Devilment(source.job==38?(source.level>=90?
Additional Effect: Grants Flourishing Starfall
Duration: 20s:):)
>> 1825, Devilment, Critical hit rate and direct hit rate are increased.
        """
        id = 16011
        name = {'Devilment', '进攻之探戈'}

    class FanDanceIii(ActionBase):
        """
Delivers an attack to target and all enemies nearby it with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Can only be executed while under the effect of Threefold Fan Dance.
>> 2052, Fan Dance III, Damage taken is reduced.
        """
        id = 16009
        name = {'扇舞·急', 'Fan Dance III'}

    class TechnicalStep(ActionBase):
        """
Begin dancing, granting yourself Technical Step.
Duration: 15s
Action changes to Technical Finish while dancing.
Only Technical Finish, En Avant, step actions, role actions, Sprint, and Limit Break can be performed while dancing.
Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
>> 2049, Technical Step, Caught up in the dance and only able to execute step actions, additional actions, Technical Finish, En Avant, Head Graze, Bolt, and Medical Kit.
>> 1819, Technical Step, Caught up in the dance and only able to execute step actions, role actions, Sprint, Limit Break, Technical Finish, and En Avant.
        """
        id = 15998
        name = {'Technical Step', '技巧舞步'}

    class TechnicalFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 350
1 Step: 540
2 Steps: 720
3 Steps: 900
4 Steps: 1,080
(source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
Damage bonus of Technical Finish varies with number of successful steps.
1 Step: 1%
2 Steps: 2%
3 Steps: 3%
4 Steps: 5%
Duration: 20s
Additional Effect: Activates the Esprit Gauge
(source.job==38?(source.level>=82?Additional Effect: Grants Flourishing Finish
Duration: 30s
:):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
(source.job==38?(source.level>=82?※Action changes to Tillana upon execution.
:):)※This action cannot be assigned to a hotbar.
>> 2050, Technical Finish, Weaponskill and spell cast and recast time are reduced.
>> 1822, Technical Finish, Damage dealt is increased.
        """
        id = 16004
        name = {'技巧舞步结束', 'Technical Finish'}

    class SingleTechnicalFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 350
1 Step: 540
2 Steps: 720
3 Steps: 900
4 Steps: 1,080
(source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
Damage bonus of Technical Finish varies with number of successful steps.
1 Step: 1%
2 Steps: 2%
3 Steps: 3%
4 Steps: 5%
Duration: 20s
(source.job==38?(source.level>=82?Additional Effect: Grants Flourishing Finish
Duration: 30s
:):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
(source.job==38?(source.level>=82?※Action changes to Tillana upon execution.
:):)※This action cannot be assigned to a hotbar.
        """
        id = 16193
        name = {'单色技巧舞步结束', 'Single Technical Finish'}

    class DoubleTechnicalFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 350
1 Step: 540
2 Steps: 720
3 Steps: 900
4 Steps: 1,080
(source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
Damage bonus of Technical Finish varies with number of successful steps.
1 Step: 1%
2 Steps: 2%
3 Steps: 3%
4 Steps: 5%
Duration: 20s
(source.job==38?(source.level>=82?Additional Effect: Grants Flourishing Finish
Duration: 30s
:):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
(source.job==38?(source.level>=82?※Action changes to Tillana upon execution.
:):)※This action cannot be assigned to a hotbar.
        """
        id = 16194
        name = {'双色技巧舞步结束', 'Double Technical Finish'}

    class TripleTechnicalFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 350
1 Step: 540
2 Steps: 720
3 Steps: 900
4 Steps: 1,080
(source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
Damage bonus of Technical Finish varies with number of successful steps.
1 Step: 1%
2 Steps: 2%
3 Steps: 3%
4 Steps: 5%
Duration: 20s
(source.job==38?(source.level>=82?Additional Effect: Grants Flourishing Finish
Duration: 30s
:):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
(source.job==38?(source.level>=82?※Action changes to Tillana upon execution.
:):)※This action cannot be assigned to a hotbar.
        """
        id = 16195
        name = {'三色技巧舞步结束', 'Triple Technical Finish'}

    class QuadrupleTechnicalFinish(ActionBase):
        """
Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
0 Steps: 350
1 Step: 540
2 Steps: 720
3 Steps: 900
4 Steps: 1,080
(source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
Damage bonus of Technical Finish varies with number of successful steps.
1 Step: 1%
2 Steps: 2%
3 Steps: 3%
4 Steps: 5%
Duration: 20s
(source.job==38?(source.level>=82?Additional Effect: Grants Flourishing Finish
Duration: 30s
:):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
(source.job==38?(source.level>=82?※Action changes to Tillana upon execution.
:):)※This action cannot be assigned to a hotbar.
        """
        id = 16196
        name = {'四色技巧舞步结束', 'Quadruple Technical Finish'}

    class Flourish(ActionBase):
        """
Grants you the effects of Flourishing Symmetry, Flourishing Flow, (source.job==38?(source.level>=86?Threefold Fan Dance, and Fourfold Fan Dance:and Threefold Fan Dance):and Threefold Fan Dance).
Can only be executed while in combat.
        """
        id = 16013
        name = {'Flourish', '百花争艳'}

    class SaberDance(ActionBase):
        """
Delivers an attack to target and all enemies nearby it with a potency of 480 for the first enemy, and 50% less for all remaining enemies.
Esprit Gauge Cost: 50
>> 2022, Saber Dance, Damage dealt is increased.
        """
        id = 16005
        name = {'剑舞', 'Saber Dance'}

    class Improvisation(ActionBase):
        """
Dance to the beat of your own drum, granting Rising Rhythm to self.
Stacks increase every 3 seconds, up to a maximum of 4.
Additional Effect: Healing over time for self and nearby party members
Cure Potency: 100
Duration: 15s
Effect ends upon using another action or moving (including facing a different direction).
Cancels auto-attack upon execution.
※Action changes to Improvised Finish upon execution.
>> 1827, Improvisation, Dancing to the beat of your own drum.
>> 1828, Improvisation, Healing magic potency is increased.
>> 2695, Improvisation, Regenerating HP over time.
        """
        id = 16014
        name = {'Improvisation', '即兴表演'}

    class ImprovisedFinish(ActionBase):
        """
Creates a barrier around self and all nearby party members. Damage absorbed increases with stacks of Rising Rhythm.
0 Stacks: 5% of maximum HP
1 Stack: 6% of maximum HP
2 Stacks: 7% of maximum HP
3 Stacks: 8% of maximum HP
4 Stacks: 10% of maximum HP
Duration: 30s
Can only be executed while Improvisation is active.
※This action cannot be assigned to a hotbar.
>> 2697, Improvised Finish, A magicked barrier is nullifying damage.
        """
        id = 25789
        name = {'Improvised Finish'}

    class Tillana(ActionBase):
        """
Delivers an attack to all nearby enemies with a potency of 360 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner
Standard Finish Effect: Increases damage dealt by 5%
Duration: 60s
Can only be executed while under the effect of Flourishing Finish.
Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
※This action cannot be assigned to a hotbar.
        """
        id = 25790
        name = {'Tillana'}

    class FanDanceIv(ActionBase):
        """
Delivers an attack to all enemies in a cone before you with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
Can only be executed while under the effect of Fourfold Fan Dance.
        """
        id = 25791
        name = {'Fan Dance IV'}

    class StarfallDance(ActionBase):
        """
Delivers a critical direct hit to all enemies in a straight line before you with a potency of 600 for the first enemy, and 75% less for all remaining enemies.
Can only be executed while under the effect of Flourishing Starfall.
        """
        id = 25792
        name = {'Starfall Dance'}