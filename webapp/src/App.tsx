import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Events from './pages/Events'
import EventDetail from './pages/EventDetail'
import Booking from './pages/Booking'
import Profile from './pages/Profile'

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-dark">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/events" element={<Events />} />
          <Route path="/events/:id" element={<EventDetail />} />
          <Route path="/booking" element={<Booking />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}
