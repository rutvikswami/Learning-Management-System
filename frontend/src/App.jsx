import React from "react";
import { Routes, Route } from "react-router-dom";
import "./App.css";

import Navbar from "./components/Navbar/Navbar";
import Home from "./pages/Home/Home";
import My_Learning from "./pages/My_Learning/My_Learning";

const App = () => {
  return (
    <div className="app">
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/my-learning/:userId/*" element={<My_Learning />} />
      </Routes>
    </div>
  );
};

export default App;
