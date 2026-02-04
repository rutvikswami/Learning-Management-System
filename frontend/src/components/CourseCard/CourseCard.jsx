import React from "react";
import "./CourseCard.css";

const CourseCard = ({ title, instructor, price, image }) => {
  return (
    <div className="course-card">
      <img src={image} alt={title} className="course-card-img" />

      <div className="course-card-body">
        <h3 className="course-title">{title}</h3>
        <p className="course-instructor">By {instructor}</p>
        <p className="course-price">₹{price}</p>

        <div className="course-card-buttons">
          <button className="enroll-btn">Enroll</button>
          <button className="details-btn">Details</button>
        </div>
      </div>
    </div>
  );
};

export default CourseCard;
