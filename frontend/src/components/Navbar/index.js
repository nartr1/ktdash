import { useState } from 'react';
import {
    IconBook,
    IconDice2,
    IconLock,
    IconSettings,
    IconUser,
    IconUsers,
} from '@tabler/icons-react';
import classes from './navbar.module.css';
import { Link, useLocation } from 'wouter';

const data = [
    { link: '/allfactions', label: 'Factions', icon: IconBook },
    { link: '/dashboard', label: 'Dashboard', icon: IconDice2 },
    { link: '/rosters', label: 'My Rosters', icon: IconUsers },
    { link: '/settings', label: 'Settings', icon: IconSettings },
];

export function NavbarSimple(props) {
    const [location] = useLocation();
    const links = data.map((item) => (
        <Link
            className={classes.link}
            data-active={item.link === location || undefined}
            href={item.link}
            key={item.label}
            onClick={() => {
                props?.close();
            }}
        >
            <item.icon className={classes.linkIcon} stroke={1.5} />
            <span>{item.label}</span>
        </Link>
    ));

    return (
        <nav className={classes.navbar}>
            <div className={classes.navbarMain}>
                {links}
            </div>

            <div className={classes.footer}>
                <Link href="/login" className={classes.link} data-active={location === "/login" || undefined} onClick={() => {
                    props?.close();
                }}>
                    <IconLock className={classes.linkIcon} stroke={1.5} />
                    <span>Log In</span>
                </Link>
                <Link href="/register" className={classes.link} data-active={location === "/register" || undefined} onClick={() => {
                    props?.close();
                }}>
                    <IconUser className={classes.linkIcon} stroke={1.5} />
                    <span>Register</span>
                </Link>
            </div>
        </nav>
    );
}