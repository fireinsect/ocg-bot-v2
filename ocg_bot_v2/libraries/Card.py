from typing import Dict, Optional


class Card(Dict):
    id: Optional[int] = None
    name: Optional[str] = None
    effect: Optional[str] = None
    zz: Optional[str] = None
    mainType: Optional[str] = None
    type: Optional[str] = None
    level: Optional[str] = None
    attribute: Optional[str] = None
    atk: Optional[str] = None
    deff: Optional[str] = None
    forbidden: Optional[str] = None

    def __getattribute__(self, item):
        if item in {'id', 'name', 'effect', 'zz', 'mainType', 'type', 'level', 'attribute', 'atk', 'deff',
                    'forbidden'}:
            if item == 'deff':
                return self['def']
            return self[item]
        return super().__getattribute__(item)
