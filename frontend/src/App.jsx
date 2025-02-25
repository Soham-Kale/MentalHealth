import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './pages/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import Services from './pages/Services';
import FormContainer from './FormContainer';
import Signup from './components/Signup';
import Login from './components/Login';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-amber-50/50 bg-gradient-to-b from-[rgb(241,232,255)] to-[rgb(228,222,254)]">
        <Navbar />
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/" element={<Login />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          <Route path="/predict" element={<FormContainer />} />
        </Routes>
        {/* <FormContainer /> */}
      </div>
    </Router>
  );
}

export default App;

