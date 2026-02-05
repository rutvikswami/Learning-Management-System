import "./CourseCardWide.css";

const CourseCardWide = ({ image, title, instructor, progress }) => {
  return (
    <div className="course-card-wide">
      <img src={image} alt={title} className="course-img" />

      <div className="course-info">
        <h3>{title}</h3>
        <p className="instructor">{instructor}</p>

        {progress !== undefined && (
          <div className="progress-box">
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{ width: `${progress}%` }}
              ></div>
            </div>
            <span>{progress}% complete</span>
          </div>
        )}
      </div>

      <div className="menu">⋮</div>
    </div>
  );
};

export default CourseCardWide;
