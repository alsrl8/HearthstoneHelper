from dataclasses import dataclass
from typing import List


@dataclass
class Card:
    id: int
    collectible: int
    slug: str
    classId: List[int]
    multiClassIds: int
    cardTypeId: int
    cardSetId: int
    rarityId: int
    artistName: str
    health: int
    attack: int
    manaCost: int
    name: str
    text: str
    image: str
    imageGold: str
    flavorText: str
    cropImage: str
    parentId: int
    childIds: List[int]
    keywordIds: List[int]
    duels: dict


@dataclass
class UnCollectibleCard:
    id: int
    collectible: int
    slug: str
    classId: int
    multiClassIds: List[int]
    cardTypeId: int
    cardSetId: int
    rarityId: int
    artistName: str
    health: int
    attack: int
    manaCost: int
    name: str
    text: str
    image: str
    imageGold: str
    flavorText: str
    cropImage: str
    parentId: int
    keywordIds: List[int]


