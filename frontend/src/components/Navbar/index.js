import { useState } from 'react';
import {
    IconBook,
    IconDice2,
    IconSettings,
    IconUser,
    IconUsers,
} from '@tabler/icons-react';
import classes from './navbar.module.css';
import { Link } from 'wouter';

const data = [
    { link: '/allfactions', label: 'Factions', icon: IconBook },
    { link: '/dashboard', label: 'Dashboard', icon: IconDice2 },
    { link: '/dashboard', label: 'My Rosters', icon: IconUsers },
    { link: '/settings', label: 'Settings', icon: IconSettings },
];

export function NavbarSimple(props) {
    const [active, setActive] = useState('Billing');
    const links = data.map((item) => (
        <Link
            className={classes.link}
            data-active={item.label === active || undefined}
            href={item.link}
            key={item.label}
            onClick={() => {
                setActive(item.label);
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

                <a href="/logout" className={classes.link} onClick={(event) => event.preventDefault()}>
                    <IconUser className={classes.linkIcon} stroke={1.5} />
                    <span>Log In</span>
                </a>
            </div>
        </nav>
    );
}