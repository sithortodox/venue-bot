import { Link } from 'react-router-dom'

export default function Profile() {
  return (
    <div className="p-4 space-y-4">
      <header className="flex items-center justify-between">
        <Link to="/" className="text-white/60">← Назад</Link>
        <h1 className="text-xl font-bold">Профиль</h1>
        <div className="w-10" />
      </header>

      <div className="card text-center">
        <div className="w-20 h-20 bg-primary/20 rounded-full flex items-center justify-center mx-auto">
          <span className="text-4xl">👤</span>
        </div>
        <h2 className="text-xl font-bold mt-3">Гость</h2>
        <p className="text-white/60 text-sm">Telegram User</p>
      </div>

      <div className="card space-y-3">
        <div className="flex justify-between">
          <span className="text-white/60">Баланс депозита</span>
          <span className="font-bold">0 ₽</span>
        </div>
        <div className="flex justify-between">
          <span className="text-white/60">Визитов</span>
          <span className="font-bold">0</span>
        </div>
      </div>

      <div className="space-y-2">
        <a href="https://t.me/venue_admin" className="btn-secondary block text-center">
          ✏️ Изменить данные
        </a>
        <Link to="/" className="btn-primary block text-center">
          ← В меню
        </Link>
      </div>
    </div>
  )
}
