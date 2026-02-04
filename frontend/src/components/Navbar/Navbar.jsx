import React, { useState } from "react";
import "./Navbar.css";
import { assets } from "../../assets/assets";


const Navbar = () => {
  const [page, setPage] = useState("home");

  return (
    <div className="navbar">
      <h2 className="logo">EduSpark</h2>
      <ul className="navbar-menu">
        <li
          onClick={() => setPage("home")}
          className={page === "home" ? "active" : ""}
        >
          Home
        </li>
        <li
          onClick={() => setPage("my_learning")}
          className={page === "my_learning" ? "active" : ""}
        >
          My Learning
        </li>
      </ul>
      <div className="navbar-right">
        <div className="navbar-search-icon">
          <input type="text" className="search-bar"/>
          <img src={assets.search_icon} alt="" className = "search-icon" />

        </div>
        <button>Sign In</button>
      </div>
    </div>
  );
};

export default Navbar;
