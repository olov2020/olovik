import React from 'react';
import "../styles/Header.css";
import Logo from "../images/logo.png";

const Header = () => {
  return (
    <div className="header">
      <p className="header__text">Who is olovik?</p>

      <img className="header__logo" src={Logo} alt="logotip"/>

      <p className="header__text">My projects</p>
    </div>
  )
}

export default Header