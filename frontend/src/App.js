import { Routes, Route } from "react-router-dom";
import { Home } from './pages/Home';
import { Login } from './pages/User/Login';
import { Signup } from './pages/User/Signup';
import { AdminLogin } from './pages/Admin/AdminLogin';
import { AdminSignup } from './pages/Admin/AdminSignup';


function App() {
  return (
    <Routes>
      <Route path="/" element={ <Home/> }/>
      <Route path="/login" element={ <Login/> }/>
      <Route path="/signup" element={ <Signup/> }/>
      <Route path="/admin/login" element={ <AdminLogin/> }/>
      <Route path="/admin/signup" element={ <AdminSignup/> }/>
    </Routes>
  );
}

export default App;
