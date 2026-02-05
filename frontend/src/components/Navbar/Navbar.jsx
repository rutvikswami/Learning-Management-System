import React from "react";
import { NavLink } from "react-router-dom";
import "./Navbar.css";
import { assets, user_data } from "../../assets/assets";

const Navbar = () => {
  
  const currentUser = user_data[0]; 

  return (
    <div className="navbar">
      <h2 className="logo">EduSpark</h2>

      <ul className="navbar-menu">
        <li>
          <NavLink
            to="/"
            className={({ isActive }) => (isActive ? "active" : "")}
          >
            Home
          </NavLink>
        </li>

        <li>
          <NavLink
            to={`/my-learning/${currentUser.userId}`}
            className={({ isActive }) => (isActive ? "active" : "")}
          >
            My Learning
          </NavLink>
        </li>
      </ul>

      <div className="navbar-right">
        <div className="navbar-search-icon">
          <input type="text" className="search-bar" />
          <img src={assets.search_icon} alt="" className="search-icon" />
        </div>

        <button>Log In</button>
        <button>Sign In</button>
      </div>
    </div>
  );
};

export default Navbar;
