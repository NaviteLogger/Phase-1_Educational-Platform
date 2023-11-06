// Header.js
import React from 'react';
import './Header.css';

function Header() {
    return (
        <header className="header">
            <div className="logo">Tu dajemy logo</div>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/courses">Courses</a></li>
                    <li><a href="/about">About Us</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
