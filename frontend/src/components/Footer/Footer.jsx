import React from "react";
import "./Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">

        {/* About */}
        <div className="footer-about">
          <h3>EduSpark</h3>
          <p>
            EduSpark is an online learning platform designed to help you gain
            industry-ready skills through expert-led courses and flexible learning.
          </p>
        </div>

        {/* Links */}
        <div className="footer-links">
          <h4>Explore</h4>
          <ul>
            <li>All Courses</li>
            <li>Top Instructors</li>
            <li>Certifications</li>
            <li>Student Reviews</li>
          </ul>
        </div>

        {/* Contact */}
        <div className="footer-contact">
          <h4>Support</h4>
          <ul>
            <li>Help Center</li>
            <li>Privacy Policy</li>
            <li>Terms & Conditions</li>
            <li>Contact Us</li>
          </ul>
        </div>

      </div>

      <div className="footer-bottom">
        © 2026 EduSpark. All rights reserved.
      </div>
    </footer>
  );
};

export default Footer;
