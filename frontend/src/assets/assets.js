import logo from "./logo.png";
import search_icon from "./search_icon.png";
import course_1 from "./course_1.png";
import course_2 from "./course_2.png";
import course_3 from "./course_3.png";
import course_4 from "./course_4.png";
import course_5 from "./course_5.png";

export const assets = {
  logo,
  search_icon,
};

export const course_list = [
  {
    _id: "1",
    title: "Python Programming",
    image: course_1,
    price: 499,
    instructor: "Dr. Angela Yu",
    description: "Learn Python from basics to advanced concepts",
    category: "Programming",
  },
  {
    _id: "2",
    title: "Web Development",
    image: course_2,
    price: 599,
    instructor: "Colt Steele",
    description: "Build modern websites using HTML CSS JavaScript",
    category: "Development",
  },
  {
    _id: "3",
    title: "AI & Machine Learning",
    image: course_3,
    price: 799,
    instructor: "Andrew Ng",
    description: "Master machine learning and artificial intelligence",
    category: "AI",
  },
  {
    _id: "4",
    title: "Data Science",
    image: course_4,
    price: 699,
    instructor: "Jose Portilla",
    description: "Analyze data using Python and statistics",
    category: "Data",
  },
  {
    _id: "5",
    title: "Cloud Computing",
    image: course_5,
    price: 649,
    instructor: "Stephane Maarek",
    description: "Understand cloud services and AWS fundamentals",
    category: "Cloud",
  }
  
];
