from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKeyConstraint,
    Index,
    Integer,
    SmallInteger,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.mysql import MEDIUMTEXT, TINYINT
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel


class Equipment(SQLModel, table=True):
    __tablename__ = "Equipment"
    __table_args__ = (Index("FK_Equipment_Killteam_idx", "factionid", "killteamid"),)

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    eqid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    fireteamid: Optional[str] = Field(sa_type=String(50), default="")
    opid: Optional[str] = Field(sa_type=String(50), default="")
    eqseq: Optional[int] = Field(sa_type=Integer, default=0)
    eqpts: Optional[str] = Field(sa_type=String(10))
    eqname: Optional[str] = Field(sa_type=String(250))
    eqdescription: Optional[str] = Field(sa_type=Text)
    eqtype: Optional[str] = Field(sa_type=String(45))
    eqvar1: Optional[str] = Field(sa_type=String(45))
    eqvar2: Optional[str] = Field(sa_type=String(45))
    eqvar3: Optional[str] = Field(sa_type=String(45))
    eqvar4: Optional[str] = Field(sa_type=String(45))
    eqcategory: Optional[str] = Field(sa_type=String(200), default="Equipment")


class Event(SQLModel, table=True):
    __tablename__ = "Event"
    __table_args__ = (
        Index("IX_TAL", "userid", "eventtype", "action", "label"),
        Index("IX_VAR1", "var1", "eventtype", "action", "label"),
        Index("IX_datestamp", "datestamp"),
    )

    eventid: Optional[int] = Field(sa_type=Integer, primary_key=True)
    datestamp: Optional[datetime] = Field(sa_type=DateTime, default=datetime.now())
    sessiontype: Optional[str] = Field(sa_type=String(50), default="")
    userid: Optional[str] = Field(sa_type=String(45))
    eventtype: Optional[str] = Field(sa_type=String(50))
    action: Optional[str] = Field(sa_type=String(45))
    label: Optional[str] = Field(sa_type=String(45))
    var1: Optional[str] = Field(sa_type=String(45))
    var2: Optional[str] = Field(sa_type=String(45))
    var3: Optional[str] = Field(sa_type=String(45))
    url: Optional[str] = Field(sa_type=String(500), default="")
    userip: Optional[str] = Field(sa_type=String(250), default="")
    useragent: Optional[str] = Field(sa_type=String(500), default="")
    referrer: Optional[str] = Field(sa_type=String(500))


# t_EventLogView = Table(
#     'EventLogView', metadata,
#     Column('eventid', Integer, server_default=text("'0'")),
#     Column('datestamp', DateTime, server_default=text("'CURRENT_TIMESTAMP'")),
#     Column('ActionLog', Text),
#     Column('userid', String(45)),
#     Column('userip', String(250)),
#     Column('eventtype', String(50)),
#     Column('action', String(45)),
#     Column('label', String(45)),
#     Column('var1', String(45)),
#     Column('var2', String(45)),
#     Column('var3', String(45)),
#     Column('username', String(250)),
#     Column('rostername', String(250)),
#     Column('opname', String(250)),
#     Column('optype', String(250))
# )


class EventBKP20240720(SQLModel, table=True):
    __tablename__ = "Event_BKP_20240720"
    __table_args__ = (
        Index("IX_TAL", "userid", "eventtype", "action", "label"),
        Index("IX_VAR1", "var1", "eventtype", "action", "label"),
        Index("IX_datestamp", "datestamp"),
    )

    eventid: Optional[int] = Field(sa_type=Integer, primary_key=True)
    datestamp: Optional[datetime] = Field(sa_type=DateTime, default=datetime.now())
    sessiontype: Optional[str] = Field(sa_type=String(50), default="")
    userid: Optional[str] = Field(sa_type=String(45))
    eventtype: Optional[str] = Field(sa_type=String(50))
    action: Optional[str] = Field(sa_type=String(45))
    label: Optional[str] = Field(sa_type=String(45))
    var1: Optional[str] = Field(sa_type=String(45))
    var2: Optional[str] = Field(sa_type=String(45))
    var3: Optional[str] = Field(sa_type=String(45))
    url: Optional[str] = Field(sa_type=String(500), default="")
    userip: Optional[str] = Field(sa_type=String(250), default="")
    useragent: Optional[str] = Field(sa_type=String(500), default="")
    referrer: Optional[str] = Field(sa_type=String(500))


class Faction(SQLModel, table=True):
    __tablename__ = "Faction"

    factionid: Optional[str] = Field(sa_type=String(10), primary_key=True)
    seq: Optional[int] = Field(sa_type=Integer)
    factionname: Optional[str] = Field(sa_type=String(250))
    description: Optional[str] = Field(sa_type=Text)

    killteams: List["Killteam"] = Relationship(back_populates="Faction_")


class Operative(SQLModel, table=True):
    __tablename__ = "Operative"
    __table_args__ = (
        Index(
            "IX_Operative_FactionIdKillTeamIdFireTeamID",
            "factionid",
            "killteamid",
            "fireteamid",
        ),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    fireteamid: Optional[str] = Field(
        sa_type=String(250), primary_key=True, nullable=False
    )
    opid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    opseq: Optional[int] = Field(sa_type=Integer, default=0)
    opname: Optional[str] = Field(sa_type=String(250))
    description: Optional[str] = Field(sa_type=Text)
    edition: Optional[str] = Field(sa_type=String(45), default="kt24")
    M: Optional[str] = Field(sa_type=String(15))
    APL: Optional[str] = Field(sa_type=String(15))
    GA: Optional[str] = Field(sa_type=String(15))
    DF: Optional[str] = Field(sa_type=String(15))
    SV: Optional[str] = Field(sa_type=String(15))
    W: Optional[str] = Field(sa_type=String(15))
    keywords: Optional[str] = Field(sa_type=String(4000))
    fireteammax: Optional[int] = Field(sa_type=Integer, default=0)
    specialisms: Optional[str] = Field(sa_type=String(50), default="")

    abilities: List["Ability"] = Relationship(back_populates="Operative_")
    uniqueactions: List["UniqueAction"] = Relationship(back_populates="Operative_")


# t_RosterOperativeView = Table(
#     'RosterOperativeView', metadata,
#     Column('userid', String(50)),
#     Column('rosterid', String(50)),
#     Column('rosteropid', String(50)),
#     Column('seq', Integer),
#     Column('opname', String(250)),
#     Column('factionid', String(50)),
#     Column('killteamid', String(50)),
#     Column('fireteamid', String(50)),
#     Column('opid', String(50)),
#     Column('hascustomportrait', Integer, server_default=text("'0'")),
#     Column('specialism', String(50)),
#     Column('isinjured', TINYINT, server_default=text("'0'")),
#     Column('rested', Integer, server_default=text("'0'")),
#     Column('M', String(15)),
#     Column('APL', String(15)),
#     Column('GA', String(15)),
#     Column('DF', String(15)),
#     Column('SV', String(15)),
#     Column('W', String(15)),
#     Column('keywords', MEDIUMTEXT),
#     Column('specialisms', String(50)),
#     Column('curW', Integer),
#     Column('activated', TINYINT, server_default=text("'0'")),
#     Column('oporder', String(45), server_default=text("'conceal'")),
#     Column('hidden', TINYINT, server_default=text("'0'")),
#     Column('wepids', String(250)),
#     Column('eqids', String(250)),
#     Column('notes', String(2000)),
#     Column('xp', Integer, server_default=text("'0'")),
#     Column('username', String(250)),
#     Column('rostername', String(250)),
#     Column('factionname', String(250)),
#     Column('killteamname', String(250)),
#     Column('edition', String(45), server_default=text("'kt24'")),
#     Column('fireteamname', String(200)),
#     Column('archetype', String(250)),
#     Column('optype', String(250))
# )


# t_RosterView = Table(
#     'RosterView', metadata,
#     Column('userid', String(50)),
#     Column('username', String(250)),
#     Column('rosterid', String(50)),
#     Column('seq', Integer),
#     Column('rostername', String(250)),
#     Column('notes', String(2000)),
#     Column('factionid', String(50)),
#     Column('killteamid', String(50)),
#     Column('hascustomportrait', Integer, server_default=text("'0'")),
#     Column('keyword', String(250)),
#     Column('portraitcopyok', Integer, server_default=text("'0'")),
#     Column('TP', Integer, server_default=text("'1'")),
#     Column('CP', Integer, server_default=text("'2'")),
#     Column('VP', Integer, server_default=text("'2'")),
#     Column('RP', Integer, server_default=text("'0'")),
#     Column('ployids', String(250)),
#     Column('tacopids', String(250)),
#     Column('spotlight', Integer, server_default=text("'0'")),
#     Column('factionname', String(250)),
#     Column('killteamname', String(250)),
#     Column('edition', String(45), server_default=text("'kt24'")),
#     Column('killteamcustomkeyword', String(250)),
#     Column('killteamdescription', Text),
#     Column('oplist', Text),
#     Column('viewcount', Integer, server_default=text("'0'")),
#     Column('importcount', Integer, server_default=text("'0'")),
#     Column('reqpts', Integer, server_default=text("'0'")),
#     Column('stratnotes', Text),
#     Column('eqnotes', Text),
#     Column('specopnotes', Text)
# )


# t_RosterView_Orig = Table(
#     'RosterView_Orig', metadata,
#     Column('userid', String(50)),
#     Column('username', String(250)),
#     Column('rosterid', String(50)),
#     Column('seq', Integer),
#     Column('rostername', String(250)),
#     Column('notes', String(2000)),
#     Column('factionid', String(50)),
#     Column('killteamid', String(50)),
#     Column('hascustomportrait', Integer, server_default=text("'0'")),
#     Column('TP', Integer, server_default=text("'1'")),
#     Column('CP', Integer, server_default=text("'2'")),
#     Column('VP', Integer, server_default=text("'2'")),
#     Column('RP', Integer, server_default=text("'0'")),
#     Column('ployids', String(250)),
#     Column('tacopids', String(250)),
#     Column('spotlight', Integer, server_default=text("'0'")),
#     Column('factionname', String(250)),
#     Column('killteamname', String(250)),
#     Column('killteamdescription', Text),
#     Column('oplist', Text),
#     Column('viewcount', Integer, server_default=text("'0'")),
#     Column('importcount', Integer, server_default=text("'0'"))
# )


class TacOp(SQLModel, table=True):
    __tablename__ = "TacOp"

    tacopid: Optional[str] = Field(sa_type=String(50), primary_key=True)
    edition: Optional[str] = Field(sa_type=String(45), default="kt21")
    archetype: Optional[str] = Field(sa_type=String(50))
    tacopseq: Optional[int] = Field(sa_type=Integer)
    title: Optional[str] = Field(sa_type=String(50))
    description: Optional[str] = Field(sa_type=String(2000))

    RosterTacOp: List["RosterTacOp"] = Relationship(back_populates="TacOp_")


class User(SQLModel, table=True):
    __tablename__ = "User"
    __table_args__ = (Index("username_UNIQUE", "username", unique=True),)

    userid: Optional[str] = Field(sa_type=String(50), primary_key=True)
    username: Optional[str] = Field(sa_type=String(250))
    passhash: Optional[str] = Field(sa_type=String(500))
    createddate: Optional[datetime] = Field(sa_type=DateTime, default=datetime.now())

    Roster: List["Roster"] = Relationship(back_populates="User_")
    Session: List["Session"] = Relationship(back_populates="User_")
    UserSetting: List["UserSetting"] = Relationship(back_populates="User_")
    RosterTacOp: List["RosterTacOp"] = Relationship(back_populates="User_")


class Weapon(SQLModel, table=True):
    __tablename__ = "Weapon"
    __table_args__ = (
        Index("FK_weapon_operative_idx", "killteamid", "fireteamid", "opid"),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    fireteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    opid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    wepid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    wepseq: Optional[int] = Field(sa_type=Integer, default=0)
    wepname: Optional[str] = Field(sa_type=String(250))
    weptype: Optional[str] = Field(sa_type=String(1))
    isdefault: Optional[int] = Field(sa_type=SmallInteger, default=0)

    weaponprofiles: List["WeaponProfile"] = Relationship(back_populates="Weapon_")


class Ability(SQLModel, table=True):
    __tablename__ = "Ability"
    __table_args__ = (
        ForeignKeyConstraint(
            ["factionid", "killteamid", "fireteamid", "opid"],
            [
                "Operative.factionid",
                "Operative.killteamid",
                "Operative.fireteamid",
                "Operative.opid",
            ],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_Ability_Operative",
        ),
        Index(
            "FK_Ability_Operative_idx", "factionid", "killteamid", "fireteamid", "opid"
        ),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    fireteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    opid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    abilityid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    title: str = Field(sa_type=String(200), nullable=False)
    description: Optional[str] = Field(sa_type=Text)

    Operative_: Optional["Operative"] = Relationship(back_populates="abilities")


class Killteam(SQLModel, table=True):
    __tablename__ = "Killteam"
    __table_args__ = (
        ForeignKeyConstraint(
            ["factionid"],
            ["Faction.factionid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_Killteam_Faction",
        ),
        Index("FK_Killteam_Faction_idx", "factionid"),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    edition: Optional[str] = Field(sa_type=String(45), default="kt24")
    killteamname: Optional[str] = Field(sa_type=String(250))
    description: Optional[str] = Field(sa_type=Text)
    killteamcomp: Optional[str] = Field(sa_type=Text)
    customkeyword: Optional[str] = Field(sa_type=String(250), default="")

    Faction_: Optional["Faction"] = Relationship(back_populates="killteams")
    Fireteam: List["Fireteam"] = Relationship(back_populates="Killteam_")
    Ploy: List["Ploy"] = Relationship(back_populates="Killteam_")


class Roster(SQLModel, table=True):
    __tablename__ = "Roster"
    __table_args__ = (
        ForeignKeyConstraint(["userid"], ["User.userid"], name="FK_Roster_User"),
        Index("IX_Roster_rosterid", "rosterid"),
        Index("rosterid_UNIQUE", "rosterid", unique=True),
    )

    userid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    rosterid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    seq: Optional[int] = Field(sa_type=Integer)
    rostername: Optional[str] = Field(sa_type=String(250))
    factionid: Optional[str] = Field(sa_type=String(50))
    killteamid: Optional[str] = Field(sa_type=String(50))
    notes: Optional[str] = Field(sa_type=String(2000), default="")
    keyword: Optional[str] = Field(sa_type=String(250), default="")
    TP: Optional[int] = Field(sa_type=Integer, default=1)
    CP: Optional[int] = Field(sa_type=Integer, default=2)
    VP: Optional[int] = Field(sa_type=Integer, default=2)
    RP: Optional[int] = Field(sa_type=Integer, default=0)
    spotlight: Optional[int] = Field(sa_type=Integer, default=0)
    hascustomportrait: Optional[int] = Field(sa_type=Integer, default=0)
    portraitcopyok: Optional[int] = Field(sa_type=Integer, default=0)
    viewcount: Optional[int] = Field(sa_type=Integer, default=0)
    importcount: Optional[int] = Field(sa_type=Integer, default=0)
    ployids: Optional[str] = Field(sa_type=String(250))
    tacopids: Optional[str] = Field(sa_type=String(250))
    reqpts: Optional[int] = Field(sa_type=Integer, default=0)
    stratnotes: Optional[str] = Field(sa_type=Text)
    eqnotes: Optional[str] = Field(sa_type=Text)
    specopnotes: Optional[str] = Field(sa_type=Text)
    createddate: Optional[datetime] = Field(sa_type=DateTime, default=datetime.now())

    User_: Optional["User"] = Relationship(back_populates="Roster")
    RosterOperative: List["RosterOperative"] = Relationship(back_populates="Roster_")
    RosterTacOp: List["RosterTacOp"] = Relationship(back_populates="Roster_")


class Session(SQLModel, table=True):
    __tablename__ = "Session"
    __table_args__ = (
        ForeignKeyConstraint(
            ["userid"],
            ["User.userid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_Session_User",
        ),
        Index("FK_Session_Player_idx", "userid"),
    )

    sessionid: Optional[str] = Field(sa_type=String(50), primary_key=True)
    userid: Optional[str] = Field(sa_type=String(50))
    lastactivity: Optional[datetime] = Field(sa_type=DateTime)

    User_: Optional["User"] = Relationship(back_populates="Session")


class UniqueAction(SQLModel, table=True):
    __tablename__ = "UniqueAction"
    __table_args__ = (
        ForeignKeyConstraint(
            ["factionid", "killteamid", "fireteamid", "opid"],
            [
                "Operative.factionid",
                "Operative.killteamid",
                "Operative.fireteamid",
                "Operative.opid",
            ],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_UniqueActions_Operative",
        ),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    fireteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    opid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    uniqueactionid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    title: Optional[str] = Field(sa_type=String(200))
    AP: Optional[int] = Field(sa_type=Integer, default=1)
    description: Optional[str] = Field(sa_type=Text)

    Operative_: Optional["Operative"] = Relationship(back_populates="uniqueactions")


class UserSetting(SQLModel, table=True):
    __tablename__ = "UserSetting"
    __table_args__ = (
        ForeignKeyConstraint(["userid"], ["User.userid"], name="FK_Setting_User"),
    )

    userid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    key: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    value: Optional[str] = Field(sa_type=String(50))

    User_: Optional["User"] = Relationship(back_populates="UserSetting")


class WeaponProfile(SQLModel, table=True):
    __tablename__ = "WeaponProfile"
    __table_args__ = (
        ForeignKeyConstraint(
            ["factionid", "killteamid", "fireteamid", "opid", "wepid"],
            [
                "Weapon.factionid",
                "Weapon.killteamid",
                "Weapon.fireteamid",
                "Weapon.opid",
                "Weapon.wepid",
            ],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_WeaponProfile_Weapon",
        ),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    fireteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    opid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    wepid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    profileid: Optional[str] = Field(
        sa_type=String(200), primary_key=True, nullable=False
    )
    name: Optional[str] = Field(sa_type=String(200))
    A: Optional[str] = Field(sa_type=String(5))
    BS: Optional[str] = Field(sa_type=String(5))
    D: Optional[str] = Field(sa_type=String(5))
    SR: Optional[str] = Field(sa_type=String(4000))

    Weapon_: Optional["Weapon"] = Relationship(back_populates="weaponprofiles")


class Fireteam(SQLModel, table=True):
    __tablename__ = "Fireteam"
    __table_args__ = (
        ForeignKeyConstraint(
            ["factionid", "killteamid"],
            ["Killteam.factionid", "Killteam.killteamid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_Fireteam_Killteam",
        ),
        Index("FK_Fireteam_Killteam_idx", "factionid", "killteamid"),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    fireteamid: Optional[str] = Field(
        sa_type=String(200), primary_key=True, nullable=False
    )
    seq: Optional[int] = Field(sa_type=Integer, default=0)
    description: Optional[str] = Field(sa_type=Text)
    killteammax: Optional[int] = Field(sa_type=Integer)
    fireteamname: Optional[str] = Field(sa_type=String(200))
    archetype: Optional[str] = Field(sa_type=String(250))
    fireteamcomp: Optional[str] = Field(sa_type=Text)

    Killteam_: Optional["Killteam"] = Relationship(back_populates="Fireteam")


class Ploy(SQLModel, table=True):
    __tablename__ = "Ploy"
    __table_args__ = (
        ForeignKeyConstraint(
            ["factionid", "killteamid"],
            ["Killteam.factionid", "Killteam.killteamid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_Ploy_Killteam",
        ),
    )

    factionid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    killteamid: Optional[str] = Field(
        sa_type=String(10), primary_key=True, nullable=False
    )
    ploytype: Optional[str] = Field(
        sa_type=String(250), primary_key=True, nullable=False
    )
    ployid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    ployname: Optional[str] = Field(sa_type=String(250))
    CP: Optional[str] = Field(sa_type=String(10))
    description: Optional[str] = Field(sa_type=Text)

    Killteam_: Optional["Killteam"] = Relationship(back_populates="Ploy")


class RosterOperative(SQLModel, table=True):
    __tablename__ = "RosterOperative"
    __table_args__ = (
        ForeignKeyConstraint(
            ["userid", "rosterid"],
            ["Roster.userid", "Roster.rosterid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_RosterOperative_Roster",
        ),
        Index("IX_RosterOperative_rosteropid", "rosteropid"),
        Index("rosteropid_UNIQUE", "rosteropid", unique=True),
    )

    userid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    rosterid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    rosteropid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    seq: Optional[int] = Field(sa_type=Integer)
    opname: Optional[str] = Field(sa_type=String(250))
    factionid: Optional[str] = Field(sa_type=String(50))
    killteamid: Optional[str] = Field(sa_type=String(50))
    fireteamid: Optional[str] = Field(sa_type=String(50))
    opid: Optional[str] = Field(sa_type=String(50))
    wepids: Optional[str] = Field(sa_type=String(250))
    eqids: Optional[str] = Field(sa_type=String(250))
    curW: Optional[int] = Field(sa_type=Integer)
    notes: Optional[str] = Field(sa_type=String(2000))
    activated: Optional[int] = Field(sa_type=TINYINT, default=0)
    hidden: Optional[int] = Field(sa_type=TINYINT, default=0)
    xp: Optional[int] = Field(sa_type=Integer, default=0)
    oporder: Optional[str] = Field(sa_type=String(45), default="conceal")
    hascustomportrait: Optional[int] = Field(sa_type=Integer, default=0)
    specialism: Optional[str] = Field(sa_type=String(50), default="")
    isinjured: Optional[int] = Field(sa_type=TINYINT, default=0)
    rested: Optional[int] = Field(sa_type=Integer, default=0)

    Roster_: Optional["Roster"] = Relationship(back_populates="RosterOperative")


class RosterTacOp(SQLModel, table=True):
    __tablename__ = "RosterTacOp"
    __table_args__ = (
        ForeignKeyConstraint(
            ["tacopid"],
            ["TacOp.tacopid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_RosterTacOp_TacOp",
        ),
        ForeignKeyConstraint(
            ["userid", "rosterid"],
            ["Roster.userid", "Roster.rosterid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_RosterTacOp_Roster",
        ),
        ForeignKeyConstraint(
            ["userid"],
            ["User.userid"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="FK_RosterTacOp_User",
        ),
        Index("FK_RosterTacOp_Roster_idx", "userid", "rosterid"),
        Index("FK_RosterTacOp_TacOp_idx", "tacopid"),
        Index("FK_RosterTacOp_User_idx", "userid"),
    )

    userid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    rosterid: Optional[str] = Field(
        sa_type=String(50), primary_key=True, nullable=False
    )
    tacopid: Optional[str] = Field(sa_type=String(50), primary_key=True, nullable=False)
    revealed: Optional[int] = Field(sa_type=TINYINT, default=0)
    VP1: Optional[int] = Field(sa_type=TINYINT, default=0)
    VP2: Optional[int] = Field(sa_type=TINYINT, default=0)

    TacOp_: Optional["TacOp"] = Relationship(back_populates="RosterTacOp")
    Roster_: Optional["Roster"] = Relationship(back_populates="RosterTacOp")
    User_: Optional["User"] = Relationship(back_populates="RosterTacOp")
