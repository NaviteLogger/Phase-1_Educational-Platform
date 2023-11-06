// Header.js
import React from 'react';
import './Header.css';

function Header() {
    return (
        <header className="header">
            <div className="logo">Tu dajemy logo</div>
            <nav>
                <ul>
                    <li><a href="/">Chata</a></li>
                    <li><a href="/courses">Kursy</a></li>
                    <li><a href="/about">O nas</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
