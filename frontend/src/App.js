import { Routes, Route } from "react-router-dom";
import { Home } from './pages/Home';
import { Login } from './pages/User/Login';
import { Signup } from './pages/User/Signup';
import { AdminLogin } from './pages/Admin/AdminLogin';
import { AdminSignup } from './pages/Admin/AdminSignup';
import { AdminDashboard } from './pages/Admin/AdminDashboard';
import { Dashboard } from "./pages/User/Dashboard";
import { GetFlightDetails } from "./pages/Flight/GetFlightDetails";


function App() {
  return (
    <Routes>
      <Route path="/" element={ <Home/> }/>
      <Route path="/login" element={ <Login/> }/>
      <Route path="/signup" element={ <Signup/> }/>
      <Route path="/admin/login" element={ <AdminLogin/> }/>
      <Route path="/admin/signup" element={ <AdminSignup/> }/>
      <Route path="/admin/dashboard" element={ <AdminDashboard/> }/>
      <Route path="/dashboard" element={ <Dashboard/> }/>
      <Route path="/get-flight-details" element={ <GetFlightDetails/> }/>
    </Routes>
  );
}

export default App;
