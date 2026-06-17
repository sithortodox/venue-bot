import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="p-4 space-y-4">
      <header className="text-center py-6">
        <h1 className="text-3xl font-bold text-primary">Venue Club</h1>
        <p className="text-white/60 mt-2">Лучшие вечеринки города</p>
      </header>

      <div className="card">
        <p className="text-white/60 text-sm">Ближайшее мероприятие</p>
        <h2 className="text-xl font-bold mt-1">Night Party</h2>
        <p className="text-white/80 mt-1">21 июня, 21:00 • Main Hall</p>
        <Link to="/events/1" className="btn-primary block text-center mt-3">
          Подробнее
        </Link>
      </div>

      <div className="grid grid-cols-2 gap-3">
        <Link to="/events" className="card text-center py-6">
          <span className="text-3xl">📅</span>
          <p className="mt-2 font-medium">Афиша</p>
        </Link>
        <Link to="/booking" className="card text-center py-6">
          <span className="text-3xl">📞</span>
          <p className="mt-2 font-medium">Бронь</p>
        </Link>
        <Link to="/profile" className="card text-center py-6">
          <span className="text-3xl">👤</span>
          <p className="mt-2 font-medium">Профиль</p>
        </Link>
        <a href="https://t.me/venue_admin" className="card text-center py-6">
          <span className="text-3xl">💬</span>
          <p className="mt-2 font-medium">Связаться</p>
        </a>
      </div>
    </div>
  )
}
