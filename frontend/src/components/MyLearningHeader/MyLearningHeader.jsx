import { NavLink } from "react-router-dom";
import "./MyLearningHeader.css";

const MyLearningHeader = ({ user }) => {
  return (
    <div className="my-learning-header">
      <h1>My learning</h1>

      <div className="learning-tabs">
        <NavLink
          to={`/my-learning/${user.userId}`}
          end
          className="tab"
        >
          All courses
        </NavLink>

        <NavLink
          to={`/my-learning/${user.userId}/mylist`}
          className="tab"
        >
          My List
        </NavLink>

        <NavLink
          to={`/my-learning/${user.userId}/wishlist`}
          className="tab"
        >
          Wishlist
        </NavLink>
      </div>
    </div>
  );
};

export default MyLearningHeader;
