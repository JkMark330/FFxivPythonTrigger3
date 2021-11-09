from typing import Optional, Union, TYPE_CHECKING, Tuple

from ..logic_data import LogicData
from ..define import HQ_FIRST

class UseAbility(object):
    def __init__(self, ability_id: int, target_id: int = None):
        self.ability_id = ability_id
        self.target_id = target_id


class UseItem(object):
    def __init__(self, item_id: int, priority: int = HQ_FIRST, target_id: int = None):
        self.item_id = item_id
        self.priority = priority
        self.target_id = target_id


class UseCommon(object):
    def __init__(self, ability_id: int, target_id: int = None):
        self.ability_id = ability_id
        self.target_id = target_id


class Strategy(object):
    name = ""
    job = ""
    fight_only: bool = True
    default_data = {}

    def __init__(self, config):
        self.config = config

    def global_cool_down_ability(self, data: LogicData) -> Optional[Union[UseAbility, UseItem, UseCommon]]:
        pass

    def non_global_cool_down_ability(self, data: LogicData) -> Optional[Union[UseAbility, UseItem, UseCommon]]:
        pass

    def common(self, data: LogicData) -> Optional[Union[UseAbility, UseItem, UseCommon]]:
        pass

    def process_ability_use(self, data: LogicData, action_id: int, target_id: int) -> Optional[Tuple[int, int]]:
        pass