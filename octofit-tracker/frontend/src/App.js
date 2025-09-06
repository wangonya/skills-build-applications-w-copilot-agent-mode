

import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import OctofitLogo from './components/OctofitLogo';


function App() {
  return (
    <Router>
      <div className="container mt-4 app-bg">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4 rounded shadow">
          <div className="d-flex align-items-center">
            <OctofitLogo />
            <Link className="navbar-brand text-light" to="/">Octofit Tracker</Link>
          </div>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item"><Link className="nav-link text-light" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link text-light" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link text-light" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link text-light" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link text-light" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </nav>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<Activities />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
