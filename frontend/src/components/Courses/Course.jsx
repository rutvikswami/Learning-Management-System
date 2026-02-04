import React from "react";
import CourseCard from "../CourseCard/CourseCard";
import "./Course.css";
import { course_list } from "../../assets/assets";

const Course = () => {
  return (
    <div className="course-display">
      <h2>Top Courses!!!</h2>

      <div className="course-lists">
        {course_list.map((item) => (
          <CourseCard
            key={item._id}
            id={item._id}
            title={item.title}
            image={item.image}
            price={item.price}
            instructor={item.instructor}
            />
        ))}
      </div>
    </div>
  );
};

export default Course;
