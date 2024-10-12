from datetime import datetime
from typing import List, Optional

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import MEDIUMTEXT, TINYINT
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel

metadata = SQLModel.metadata


class Equipment(SQLModel, table=True):
    __tablename__ = 'Equipment'
    __table_args__ = (
        Index('FK_Equipment_Killteam_idx', 'factionid', 'killteamid'),
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    eqid: Optional[str] = Field(default=None, sa_column=mapped_column('eqid', String(50), primary_key=True, nullable=False))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(50), server_default=text("''")))
    opid: Optional[str] = Field(default=None, sa_column=mapped_column('opid', String(50), server_default=text("''")))
    eqseq: Optional[int] = Field(default=None, sa_column=mapped_column('eqseq', Integer, server_default=text("'0'")))
    eqpts: Optional[str] = Field(default=None, sa_column=mapped_column('eqpts', String(10)))
    eqname: Optional[str] = Field(default=None, sa_column=mapped_column('eqname', String(250)))
    eqdescription: Optional[str] = Field(default=None, sa_column=mapped_column('eqdescription', Text))
    eqtype: Optional[str] = Field(default=None, sa_column=mapped_column('eqtype', String(45)))
    eqvar1: Optional[str] = Field(default=None, sa_column=mapped_column('eqvar1', String(45)))
    eqvar2: Optional[str] = Field(default=None, sa_column=mapped_column('eqvar2', String(45)))
    eqvar3: Optional[str] = Field(default=None, sa_column=mapped_column('eqvar3', String(45)))
    eqvar4: Optional[str] = Field(default=None, sa_column=mapped_column('eqvar4', String(45)))
    eqcategory: Optional[str] = Field(default=None, sa_column=mapped_column('eqcategory', String(200), server_default=text("'Equipment'")))


class Event(SQLModel, table=True):
    __tablename__ = 'Event'
    __table_args__ = (
        Index('IX_TAL', 'userid', 'eventtype', 'action', 'label'),
        Index('IX_VAR1', 'var1', 'eventtype', 'action', 'label'),
        Index('IX_datestamp', 'datestamp')
    )

    eventid: Optional[int] = Field(default=None, sa_column=mapped_column('eventid', Integer, primary_key=True))
    datestamp: Optional[datetime] = Field(default=None, sa_column=mapped_column('datestamp', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    sessiontype: Optional[str] = Field(default=None, sa_column=mapped_column('sessiontype', String(50), server_default=text("''")))
    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(45)))
    eventtype: Optional[str] = Field(default=None, sa_column=mapped_column('eventtype', String(50)))
    action: Optional[str] = Field(default=None, sa_column=mapped_column('action', String(45)))
    label: Optional[str] = Field(default=None, sa_column=mapped_column('label', String(45)))
    var1: Optional[str] = Field(default=None, sa_column=mapped_column('var1', String(45)))
    var2: Optional[str] = Field(default=None, sa_column=mapped_column('var2', String(45)))
    var3: Optional[str] = Field(default=None, sa_column=mapped_column('var3', String(45)))
    url: Optional[str] = Field(default=None, sa_column=mapped_column('url', String(500), server_default=text("''")))
    userip: Optional[str] = Field(default=None, sa_column=mapped_column('userip', String(250), server_default=text("''")))
    useragent: Optional[str] = Field(default=None, sa_column=mapped_column('useragent', String(500), server_default=text("''")))
    referrer: Optional[str] = Field(default=None, sa_column=mapped_column('referrer', String(500)))


t_EventLogView = Table(
    'EventLogView', metadata,
    Column('eventid', Integer, server_default=text("'0'")),
    Column('datestamp', DateTime, server_default=text("'CURRENT_TIMESTAMP'")),
    Column('ActionLog', Text),
    Column('userid', String(45)),
    Column('userip', String(250)),
    Column('eventtype', String(50)),
    Column('action', String(45)),
    Column('label', String(45)),
    Column('var1', String(45)),
    Column('var2', String(45)),
    Column('var3', String(45)),
    Column('username', String(250)),
    Column('rostername', String(250)),
    Column('opname', String(250)),
    Column('optype', String(250))
)


class EventBKP20240720(SQLModel, table=True):
    __tablename__ = 'Event_BKP_20240720'
    __table_args__ = (
        Index('IX_TAL', 'userid', 'eventtype', 'action', 'label'),
        Index('IX_VAR1', 'var1', 'eventtype', 'action', 'label'),
        Index('IX_datestamp', 'datestamp')
    )

    eventid: Optional[int] = Field(default=None, sa_column=mapped_column('eventid', Integer, primary_key=True))
    datestamp: Optional[datetime] = Field(default=None, sa_column=mapped_column('datestamp', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    sessiontype: Optional[str] = Field(default=None, sa_column=mapped_column('sessiontype', String(50), server_default=text("''")))
    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(45)))
    eventtype: Optional[str] = Field(default=None, sa_column=mapped_column('eventtype', String(50)))
    action: Optional[str] = Field(default=None, sa_column=mapped_column('action', String(45)))
    label: Optional[str] = Field(default=None, sa_column=mapped_column('label', String(45)))
    var1: Optional[str] = Field(default=None, sa_column=mapped_column('var1', String(45)))
    var2: Optional[str] = Field(default=None, sa_column=mapped_column('var2', String(45)))
    var3: Optional[str] = Field(default=None, sa_column=mapped_column('var3', String(45)))
    url: Optional[str] = Field(default=None, sa_column=mapped_column('url', String(500), server_default=text("''")))
    userip: Optional[str] = Field(default=None, sa_column=mapped_column('userip', String(250), server_default=text("''")))
    useragent: Optional[str] = Field(default=None, sa_column=mapped_column('useragent', String(500), server_default=text("''")))
    referrer: Optional[str] = Field(default=None, sa_column=mapped_column('referrer', String(500)))


class Faction(SQLModel, table=True):
    __tablename__ = 'Faction'

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True))
    seq: Optional[int] = Field(default=None, sa_column=mapped_column('seq', Integer))
    factionname: Optional[str] = Field(default=None, sa_column=mapped_column('factionname', String(250)))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))

    Killteam: List['Killteam'] = Relationship(back_populates='Faction_')


class Operative(SQLModel, table=True):
    __tablename__ = 'Operative'
    __table_args__ = (
        Index('IX_Operative_FactionIdKillTeamIdFireTeamID', 'factionid', 'killteamid', 'fireteamid'),
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(250), primary_key=True, nullable=False))
    opid: Optional[str] = Field(default=None, sa_column=mapped_column('opid', String(50), primary_key=True, nullable=False))
    opseq: Optional[int] = Field(default=None, sa_column=mapped_column('opseq', Integer, server_default=text("'0'")))
    opname: Optional[str] = Field(default=None, sa_column=mapped_column('opname', String(250)))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    edition: Optional[str] = Field(default=None, sa_column=mapped_column('edition', String(45), server_default=text("'kt24'")))
    M: Optional[str] = Field(default=None, sa_column=mapped_column('M', String(15)))
    APL: Optional[str] = Field(default=None, sa_column=mapped_column('APL', String(15)))
    GA: Optional[str] = Field(default=None, sa_column=mapped_column('GA', String(15)))
    DF: Optional[str] = Field(default=None, sa_column=mapped_column('DF', String(15)))
    SV: Optional[str] = Field(default=None, sa_column=mapped_column('SV', String(15)))
    W: Optional[str] = Field(default=None, sa_column=mapped_column('W', String(15)))
    keywords: Optional[str] = Field(default=None, sa_column=mapped_column('keywords', String(4000)))
    fireteammax: Optional[int] = Field(default=None, sa_column=mapped_column('fireteammax', Integer, server_default=text("'0'")))
    specialisms: Optional[str] = Field(default=None, sa_column=mapped_column('specialisms', String(50), server_default=text("''")))

    Ability: List['Ability'] = Relationship(back_populates='Operative_')
    UniqueAction: List['UniqueAction'] = Relationship(back_populates='Operative_')


t_RosterOperativeView = Table(
    'RosterOperativeView', metadata,
    Column('userid', String(50)),
    Column('rosterid', String(50)),
    Column('rosteropid', String(50)),
    Column('seq', Integer),
    Column('opname', String(250)),
    Column('factionid', String(50)),
    Column('killteamid', String(50)),
    Column('fireteamid', String(50)),
    Column('opid', String(50)),
    Column('hascustomportrait', Integer, server_default=text("'0'")),
    Column('specialism', String(50)),
    Column('isinjured', TINYINT, server_default=text("'0'")),
    Column('rested', Integer, server_default=text("'0'")),
    Column('M', String(15)),
    Column('APL', String(15)),
    Column('GA', String(15)),
    Column('DF', String(15)),
    Column('SV', String(15)),
    Column('W', String(15)),
    Column('keywords', MEDIUMTEXT),
    Column('specialisms', String(50)),
    Column('curW', Integer),
    Column('activated', TINYINT, server_default=text("'0'")),
    Column('oporder', String(45), server_default=text("'conceal'")),
    Column('hidden', TINYINT, server_default=text("'0'")),
    Column('wepids', String(250)),
    Column('eqids', String(250)),
    Column('notes', String(2000)),
    Column('xp', Integer, server_default=text("'0'")),
    Column('username', String(250)),
    Column('rostername', String(250)),
    Column('factionname', String(250)),
    Column('killteamname', String(250)),
    Column('edition', String(45), server_default=text("'kt24'")),
    Column('fireteamname', String(200)),
    Column('archetype', String(250)),
    Column('optype', String(250))
)


t_RosterView = Table(
    'RosterView', metadata,
    Column('userid', String(50)),
    Column('username', String(250)),
    Column('rosterid', String(50)),
    Column('seq', Integer),
    Column('rostername', String(250)),
    Column('notes', String(2000)),
    Column('factionid', String(50)),
    Column('killteamid', String(50)),
    Column('hascustomportrait', Integer, server_default=text("'0'")),
    Column('keyword', String(250)),
    Column('portraitcopyok', Integer, server_default=text("'0'")),
    Column('TP', Integer, server_default=text("'1'")),
    Column('CP', Integer, server_default=text("'2'")),
    Column('VP', Integer, server_default=text("'2'")),
    Column('RP', Integer, server_default=text("'0'")),
    Column('ployids', String(250)),
    Column('tacopids', String(250)),
    Column('spotlight', Integer, server_default=text("'0'")),
    Column('factionname', String(250)),
    Column('killteamname', String(250)),
    Column('edition', String(45), server_default=text("'kt24'")),
    Column('killteamcustomkeyword', String(250)),
    Column('killteamdescription', Text),
    Column('oplist', Text),
    Column('viewcount', Integer, server_default=text("'0'")),
    Column('importcount', Integer, server_default=text("'0'")),
    Column('reqpts', Integer, server_default=text("'0'")),
    Column('stratnotes', Text),
    Column('eqnotes', Text),
    Column('specopnotes', Text)
)


t_RosterView_Orig = Table(
    'RosterView_Orig', metadata,
    Column('userid', String(50)),
    Column('username', String(250)),
    Column('rosterid', String(50)),
    Column('seq', Integer),
    Column('rostername', String(250)),
    Column('notes', String(2000)),
    Column('factionid', String(50)),
    Column('killteamid', String(50)),
    Column('hascustomportrait', Integer, server_default=text("'0'")),
    Column('TP', Integer, server_default=text("'1'")),
    Column('CP', Integer, server_default=text("'2'")),
    Column('VP', Integer, server_default=text("'2'")),
    Column('RP', Integer, server_default=text("'0'")),
    Column('ployids', String(250)),
    Column('tacopids', String(250)),
    Column('spotlight', Integer, server_default=text("'0'")),
    Column('factionname', String(250)),
    Column('killteamname', String(250)),
    Column('killteamdescription', Text),
    Column('oplist', Text),
    Column('viewcount', Integer, server_default=text("'0'")),
    Column('importcount', Integer, server_default=text("'0'"))
)


class TacOp(SQLModel, table=True):
    __tablename__ = 'TacOp'

    tacopid: Optional[str] = Field(default=None, sa_column=mapped_column('tacopid', String(50), primary_key=True))
    edition: Optional[str] = Field(default=None, sa_column=mapped_column('edition', String(45), server_default=text("'kt21'")))
    archetype: Optional[str] = Field(default=None, sa_column=mapped_column('archetype', String(50)))
    tacopseq: Optional[int] = Field(default=None, sa_column=mapped_column('tacopseq', Integer))
    title: Optional[str] = Field(default=None, sa_column=mapped_column('title', String(50)))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', String(2000)))

    RosterTacOp: List['RosterTacOp'] = Relationship(back_populates='TacOp_')


class User(SQLModel, table=True):
    __tablename__ = 'User'
    __table_args__ = (
        Index('username_UNIQUE', 'username', unique=True),
    )

    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(50), primary_key=True))
    username: Optional[str] = Field(default=None, sa_column=mapped_column('username', String(250)))
    passhash: Optional[str] = Field(default=None, sa_column=mapped_column('passhash', String(500)))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))

    Roster: List['Roster'] = Relationship(back_populates='User_')
    Session: List['Session'] = Relationship(back_populates='User_')
    UserSetting: List['UserSetting'] = Relationship(back_populates='User_')
    RosterTacOp: List['RosterTacOp'] = Relationship(back_populates='User_')


class Weapon(SQLModel, table=True):
    __tablename__ = 'Weapon'
    __table_args__ = (
        Index('FK_weapon_operative_idx', 'killteamid', 'fireteamid', 'opid'),
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(50), primary_key=True, nullable=False))
    opid: Optional[str] = Field(default=None, sa_column=mapped_column('opid', String(50), primary_key=True, nullable=False))
    wepid: Optional[str] = Field(default=None, sa_column=mapped_column('wepid', String(50), primary_key=True, nullable=False))
    wepseq: Optional[int] = Field(default=None, sa_column=mapped_column('wepseq', Integer, server_default=text("'0'")))
    wepname: Optional[str] = Field(default=None, sa_column=mapped_column('wepname', String(250)))
    weptype: Optional[str] = Field(default=None, sa_column=mapped_column('weptype', String(1)))
    isdefault: Optional[int] = Field(default=None, sa_column=mapped_column('isdefault', SmallInteger, server_default=text("'0'")))

    WeaponProfile: List['WeaponProfile'] = Relationship(back_populates='Weapon_')


class Ability(SQLModel, table=True):
    __tablename__ = 'Ability'
    __table_args__ = (
        ForeignKeyConstraint(['factionid', 'killteamid', 'fireteamid', 'opid'], ['Operative.factionid', 'Operative.killteamid', 'Operative.fireteamid', 'Operative.opid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_Ability_Operative'),
        Index('FK_Ability_Operative_idx', 'factionid', 'killteamid', 'fireteamid', 'opid')
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(50), primary_key=True, nullable=False))
    opid: Optional[str] = Field(default=None, sa_column=mapped_column('opid', String(50), primary_key=True, nullable=False))
    abilityid: Optional[str] = Field(default=None, sa_column=mapped_column('abilityid', String(50), primary_key=True, nullable=False))
    title: str = Field(sa_column=mapped_column('title', String(200), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))

    Operative_: Optional['Operative'] = Relationship(back_populates='Ability')


class Killteam(SQLModel, table=True):
    __tablename__ = 'Killteam'
    __table_args__ = (
        ForeignKeyConstraint(['factionid'], ['Faction.factionid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_Killteam_Faction'),
        Index('FK_Killteam_Faction_idx', 'factionid')
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    edition: Optional[str] = Field(default=None, sa_column=mapped_column('edition', String(45), server_default=text("'kt24'")))
    killteamname: Optional[str] = Field(default=None, sa_column=mapped_column('killteamname', String(250)))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    killteamcomp: Optional[str] = Field(default=None, sa_column=mapped_column('killteamcomp', Text))
    customkeyword: Optional[str] = Field(default=None, sa_column=mapped_column('customkeyword', String(250), server_default=text("''")))

    Faction_: Optional['Faction'] = Relationship(back_populates='Killteam')
    Fireteam: List['Fireteam'] = Relationship(back_populates='Killteam_')
    Ploy: List['Ploy'] = Relationship(back_populates='Killteam_')


class Roster(SQLModel, table=True):
    __tablename__ = 'Roster'
    __table_args__ = (
        ForeignKeyConstraint(['userid'], ['User.userid'], name='FK_Roster_User'),
        Index('IX_Roster_rosterid', 'rosterid'),
        Index('rosterid_UNIQUE', 'rosterid', unique=True)
    )

    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(50), primary_key=True, nullable=False))
    rosterid: Optional[str] = Field(default=None, sa_column=mapped_column('rosterid', String(50), primary_key=True, nullable=False))
    seq: Optional[int] = Field(default=None, sa_column=mapped_column('seq', Integer))
    rostername: Optional[str] = Field(default=None, sa_column=mapped_column('rostername', String(250)))
    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(50)))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50)))
    notes: Optional[str] = Field(default=None, sa_column=mapped_column('notes', String(2000), server_default=text("''")))
    keyword: Optional[str] = Field(default=None, sa_column=mapped_column('keyword', String(250), server_default=text("''")))
    TP: Optional[int] = Field(default=None, sa_column=mapped_column('TP', Integer, server_default=text("'1'")))
    CP: Optional[int] = Field(default=None, sa_column=mapped_column('CP', Integer, server_default=text("'2'")))
    VP: Optional[int] = Field(default=None, sa_column=mapped_column('VP', Integer, server_default=text("'2'")))
    RP: Optional[int] = Field(default=None, sa_column=mapped_column('RP', Integer, server_default=text("'0'")))
    spotlight: Optional[int] = Field(default=None, sa_column=mapped_column('spotlight', Integer, server_default=text("'0'")))
    hascustomportrait: Optional[int] = Field(default=None, sa_column=mapped_column('hascustomportrait', Integer, server_default=text("'0'")))
    portraitcopyok: Optional[int] = Field(default=None, sa_column=mapped_column('portraitcopyok', Integer, server_default=text("'0'")))
    viewcount: Optional[int] = Field(default=None, sa_column=mapped_column('viewcount', Integer, server_default=text("'0'")))
    importcount: Optional[int] = Field(default=None, sa_column=mapped_column('importcount', Integer, server_default=text("'0'")))
    ployids: Optional[str] = Field(default=None, sa_column=mapped_column('ployids', String(250)))
    tacopids: Optional[str] = Field(default=None, sa_column=mapped_column('tacopids', String(250)))
    reqpts: Optional[int] = Field(default=None, sa_column=mapped_column('reqpts', Integer, server_default=text("'0'")))
    stratnotes: Optional[str] = Field(default=None, sa_column=mapped_column('stratnotes', Text))
    eqnotes: Optional[str] = Field(default=None, sa_column=mapped_column('eqnotes', Text))
    specopnotes: Optional[str] = Field(default=None, sa_column=mapped_column('specopnotes', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))

    User_: Optional['User'] = Relationship(back_populates='Roster')
    RosterOperative: List['RosterOperative'] = Relationship(back_populates='Roster_')
    RosterTacOp: List['RosterTacOp'] = Relationship(back_populates='Roster_')


class Session(SQLModel, table=True):
    __tablename__ = 'Session'
    __table_args__ = (
        ForeignKeyConstraint(['userid'], ['User.userid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_Session_User'),
        Index('FK_Session_Player_idx', 'userid')
    )

    sessionid: Optional[str] = Field(default=None, sa_column=mapped_column('sessionid', String(50), primary_key=True))
    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(50)))
    lastactivity: Optional[datetime] = Field(default=None, sa_column=mapped_column('lastactivity', DateTime))

    User_: Optional['User'] = Relationship(back_populates='Session')


class UniqueAction(SQLModel, table=True):
    __tablename__ = 'UniqueAction'
    __table_args__ = (
        ForeignKeyConstraint(['factionid', 'killteamid', 'fireteamid', 'opid'], ['Operative.factionid', 'Operative.killteamid', 'Operative.fireteamid', 'Operative.opid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_UniqueActions_Operative'),
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(50), primary_key=True, nullable=False))
    opid: Optional[str] = Field(default=None, sa_column=mapped_column('opid', String(50), primary_key=True, nullable=False))
    uniqueactionid: Optional[str] = Field(default=None, sa_column=mapped_column('uniqueactionid', String(50), primary_key=True, nullable=False))
    title: Optional[str] = Field(default=None, sa_column=mapped_column('title', String(200)))
    AP: Optional[int] = Field(default=None, sa_column=mapped_column('AP', Integer, server_default=text("'1'")))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))

    Operative_: Optional['Operative'] = Relationship(back_populates='UniqueAction')


class UserSetting(SQLModel, table=True):
    __tablename__ = 'UserSetting'
    __table_args__ = (
        ForeignKeyConstraint(['userid'], ['User.userid'], name='FK_Setting_User'),
    )

    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(50), primary_key=True, nullable=False))
    key: Optional[str] = Field(default=None, sa_column=mapped_column('key', String(50), primary_key=True, nullable=False))
    value: Optional[str] = Field(default=None, sa_column=mapped_column('value', String(50)))

    User_: Optional['User'] = Relationship(back_populates='UserSetting')


class WeaponProfile(SQLModel, table=True):
    __tablename__ = 'WeaponProfile'
    __table_args__ = (
        ForeignKeyConstraint(['factionid', 'killteamid', 'fireteamid', 'opid', 'wepid'], ['Weapon.factionid', 'Weapon.killteamid', 'Weapon.fireteamid', 'Weapon.opid', 'Weapon.wepid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_WeaponProfile_Weapon'),
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(50), primary_key=True, nullable=False))
    opid: Optional[str] = Field(default=None, sa_column=mapped_column('opid', String(50), primary_key=True, nullable=False))
    wepid: Optional[str] = Field(default=None, sa_column=mapped_column('wepid', String(50), primary_key=True, nullable=False))
    profileid: Optional[str] = Field(default=None, sa_column=mapped_column('profileid', String(200), primary_key=True, nullable=False))
    name: Optional[str] = Field(default=None, sa_column=mapped_column('name', String(200)))
    A: Optional[str] = Field(default=None, sa_column=mapped_column('A', String(5)))
    BS: Optional[str] = Field(default=None, sa_column=mapped_column('BS', String(5)))
    D: Optional[str] = Field(default=None, sa_column=mapped_column('D', String(5)))
    SR: Optional[str] = Field(default=None, sa_column=mapped_column('SR', String(4000)))

    Weapon_: Optional['Weapon'] = Relationship(back_populates='WeaponProfile')


class Fireteam(SQLModel, table=True):
    __tablename__ = 'Fireteam'
    __table_args__ = (
        ForeignKeyConstraint(['factionid', 'killteamid'], ['Killteam.factionid', 'Killteam.killteamid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_Fireteam_Killteam'),
        Index('FK_Fireteam_Killteam_idx', 'factionid', 'killteamid')
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50), primary_key=True, nullable=False))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(200), primary_key=True, nullable=False))
    seq: Optional[int] = Field(default=None, sa_column=mapped_column('seq', Integer, server_default=text("'0'")))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    killteammax: Optional[int] = Field(default=None, sa_column=mapped_column('killteammax', Integer))
    fireteamname: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamname', String(200)))
    archetype: Optional[str] = Field(default=None, sa_column=mapped_column('archetype', String(250)))
    fireteamcomp: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamcomp', Text))

    Killteam_: Optional['Killteam'] = Relationship(back_populates='Fireteam')


class Ploy(SQLModel, table=True):
    __tablename__ = 'Ploy'
    __table_args__ = (
        ForeignKeyConstraint(['factionid', 'killteamid'], ['Killteam.factionid', 'Killteam.killteamid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_Ploy_Killteam'),
    )

    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(10), primary_key=True, nullable=False))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(10), primary_key=True, nullable=False))
    ploytype: Optional[str] = Field(default=None, sa_column=mapped_column('ploytype', String(250), primary_key=True, nullable=False))
    ployid: Optional[str] = Field(default=None, sa_column=mapped_column('ployid', String(50), primary_key=True, nullable=False))
    ployname: Optional[str] = Field(default=None, sa_column=mapped_column('ployname', String(250)))
    CP: Optional[str] = Field(default=None, sa_column=mapped_column('CP', String(10)))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))

    Killteam_: Optional['Killteam'] = Relationship(back_populates='Ploy')


class RosterOperative(SQLModel, table=True):
    __tablename__ = 'RosterOperative'
    __table_args__ = (
        ForeignKeyConstraint(['userid', 'rosterid'], ['Roster.userid', 'Roster.rosterid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_RosterOperative_Roster'),
        Index('IX_RosterOperative_rosteropid', 'rosteropid'),
        Index('rosteropid_UNIQUE', 'rosteropid', unique=True)
    )

    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(50), primary_key=True, nullable=False))
    rosterid: Optional[str] = Field(default=None, sa_column=mapped_column('rosterid', String(50), primary_key=True, nullable=False))
    rosteropid: Optional[str] = Field(default=None, sa_column=mapped_column('rosteropid', String(50), primary_key=True, nullable=False))
    seq: Optional[int] = Field(default=None, sa_column=mapped_column('seq', Integer))
    opname: Optional[str] = Field(default=None, sa_column=mapped_column('opname', String(250)))
    factionid: Optional[str] = Field(default=None, sa_column=mapped_column('factionid', String(50)))
    killteamid: Optional[str] = Field(default=None, sa_column=mapped_column('killteamid', String(50)))
    fireteamid: Optional[str] = Field(default=None, sa_column=mapped_column('fireteamid', String(50)))
    opid: Optional[str] = Field(default=None, sa_column=mapped_column('opid', String(50)))
    wepids: Optional[str] = Field(default=None, sa_column=mapped_column('wepids', String(250)))
    eqids: Optional[str] = Field(default=None, sa_column=mapped_column('eqids', String(250)))
    curW: Optional[int] = Field(default=None, sa_column=mapped_column('curW', Integer))
    notes: Optional[str] = Field(default=None, sa_column=mapped_column('notes', String(2000)))
    activated: Optional[int] = Field(default=None, sa_column=mapped_column('activated', TINYINT, server_default=text("'0'")))
    hidden: Optional[int] = Field(default=None, sa_column=mapped_column('hidden', TINYINT, server_default=text("'0'")))
    xp: Optional[int] = Field(default=None, sa_column=mapped_column('xp', Integer, server_default=text("'0'")))
    oporder: Optional[str] = Field(default=None, sa_column=mapped_column('oporder', String(45), server_default=text("'conceal'")))
    hascustomportrait: Optional[int] = Field(default=None, sa_column=mapped_column('hascustomportrait', Integer, server_default=text("'0'")))
    specialism: Optional[str] = Field(default=None, sa_column=mapped_column('specialism', String(50), server_default=text("''")))
    isinjured: Optional[int] = Field(default=None, sa_column=mapped_column('isinjured', TINYINT, server_default=text("'0'")))
    rested: Optional[int] = Field(default=None, sa_column=mapped_column('rested', Integer, server_default=text("'0'")))

    Roster_: Optional['Roster'] = Relationship(back_populates='RosterOperative')


class RosterTacOp(SQLModel, table=True):
    __tablename__ = 'RosterTacOp'
    __table_args__ = (
        ForeignKeyConstraint(['tacopid'], ['TacOp.tacopid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_RosterTacOp_TacOp'),
        ForeignKeyConstraint(['userid', 'rosterid'], ['Roster.userid', 'Roster.rosterid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_RosterTacOp_Roster'),
        ForeignKeyConstraint(['userid'], ['User.userid'], ondelete='CASCADE', onupdate='CASCADE', name='FK_RosterTacOp_User'),
        Index('FK_RosterTacOp_Roster_idx', 'userid', 'rosterid'),
        Index('FK_RosterTacOp_TacOp_idx', 'tacopid'),
        Index('FK_RosterTacOp_User_idx', 'userid')
    )

    userid: Optional[str] = Field(default=None, sa_column=mapped_column('userid', String(50), primary_key=True, nullable=False))
    rosterid: Optional[str] = Field(default=None, sa_column=mapped_column('rosterid', String(50), primary_key=True, nullable=False))
    tacopid: Optional[str] = Field(default=None, sa_column=mapped_column('tacopid', String(50), primary_key=True, nullable=False))
    revealed: Optional[int] = Field(default=None, sa_column=mapped_column('revealed', TINYINT, server_default=text("'0'")))
    VP1: Optional[int] = Field(default=None, sa_column=mapped_column('VP1', TINYINT, server_default=text("'0'")))
    VP2: Optional[int] = Field(default=None, sa_column=mapped_column('VP2', TINYINT, server_default=text("'0'")))

    TacOp_: Optional['TacOp'] = Relationship(back_populates='RosterTacOp')
    Roster_: Optional['Roster'] = Relationship(back_populates='RosterTacOp')
    User_: Optional['User'] = Relationship(back_populates='RosterTacOp')
