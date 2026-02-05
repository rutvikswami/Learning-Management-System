import React from "react";
import { Routes, Route, useParams } from "react-router-dom";
import { user_data } from "../../assets/assets";

import MyLearningHeader from "../../components/MyLearningHeader/MyLearningHeader";
import All_Courses from "../../components/All_Courses/All_Courses";
import Wishlist from "../../components/Wishlist/Wishlist";
import MyList from "../../components/MyList/MyList";
import "./My_Learning.css";

const My_Learning = () => {
  const { userId } = useParams();

  const currentUser = user_data.find(
    (user) => user.userId === userId
  );

  if (!currentUser) {
    return <h2>User not found</h2>;
  }

  return (
    <>
      <MyLearningHeader user={currentUser} />

      <div className="learning-content">
        <Routes>
          <Route
            path="/"
            element={<All_Courses user={currentUser} />}
          />
          <Route
            path="wishlist"
            element={<Wishlist user={currentUser} />}
          />
          <Route
            path="mylist"
            element={<MyList user={currentUser} />}
          />
        </Routes>
      </div>
    </>
  );
};

export default My_Learning;
