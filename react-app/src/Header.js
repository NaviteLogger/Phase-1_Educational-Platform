// Header.js
import React from 'react';
import './Header.css';

function Header() {
    return (
        <header className="header">
            <div className='leftBox'>
                <img src='' alt='logo' />
            </div>
            <div className='middleBox'>
                <nav>Strona Główna</nav>
                <nav>Oferta</nav>
                <nav>Kontakt</nav>
                <nav>O nas</nav>
            </div>
            <div className='rightBox'></div>


        </header>
    );
}

export default Header;
