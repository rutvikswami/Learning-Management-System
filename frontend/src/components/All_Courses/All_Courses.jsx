import { course_list, user_list } from "../../assets/assets";
import CourseCardWide from "../../components/CourseCardWide/CourseCardWide";
import { useParams } from "react-router-dom";

const All_Courses = () => {
  const { userId } = useParams();
  const user = user_list.find(u => u.userId === userId);

  return (
    <div>
      {user.enrolledCourses.map(item => {
        const course = course_list.find(
          c => c._id === item.courseId
        );

        return (
          <CourseCardWide
            key={course._id}
            title={course.title}
            instructor={course.instructor}
            image={course.image}
            progress={item.progress}
          />
        );
      })}
    </div>
  );
};

export default All_Courses;
