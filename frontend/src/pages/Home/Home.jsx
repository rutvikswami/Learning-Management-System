import React from 'react'
import './Home.css'
import Header from '../../components/Header/Header'
import Course from '../../components/Courses/Course'
import Footer from '../../components/Footer/Footer'

const Home = () => {

  return (
    <div >
        <Header/>
        <Course/>
        <Footer/>
    </div>
  )

}

export default Home