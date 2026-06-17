import { useState } from 'react'
import { Link } from 'react-router-dom'

export default function Booking() {
  const [form, setForm] = useState({
    event: '',
    name: '',
    phone: '',
    guests: '2',
  })
  const [submitted, setSubmitted] = useState(false)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    setSubmitted(true)
  }

  if (submitted) {
    return (
      <div className="p-4 text-center space-y-4">
        <div className="text-6xl">✅</div>
        <h1 className="text-2xl font-bold">Заявка отправлена!</h1>
        <p className="text-white/60">
          Наш администратор свяжется с вами в ближайшее время
        </p>
        <Link to="/" className="btn-primary inline-block">
          В меню
        </Link>
      </div>
    )
  }

  return (
    <div className="p-4 space-y-4">
      <header className="flex items-center justify-between">
        <Link to="/" className="text-white/60">← Назад</Link>
        <h1 className="text-xl font-bold">Бронирование</h1>
        <div className="w-10" />
      </header>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="card space-y-3">
          <div>
            <label className="text-white/60 text-sm block mb-1">Мероприятие</label>
            <select
              className="input-field"
              value={form.event}
              onChange={(e) => setForm({ ...form, event: e.target.value })}
              required
            >
              <option value="">Выберите мероприятие</option>
              <option value="Night Party">Night Party — 21 июня</option>
              <option value="Lounge Evening">Lounge Evening — 23 июня</option>
              <option value="VIP Night">VIP Night — 25 июня</option>
              <option value="Rooftop Sunset">Rooftop Sunset — 28 июня</option>
            </select>
          </div>

          <div>
            <label className="text-white/60 text-sm block mb-1">Ваше имя</label>
            <input
              type="text"
              className="input-field"
              placeholder="Иван"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
              required
            />
          </div>

          <div>
            <label className="text-white/60 text-sm block mb-1">Телефон</label>
            <input
              type="tel"
              className="input-field"
              placeholder="+7 (999) 123-45-67"
              value={form.phone}
              onChange={(e) => setForm({ ...form, phone: e.target.value })}
              required
            />
          </div>

          <div>
            <label className="text-white/60 text-sm block mb-1">Количество гостей</label>
            <div className="flex items-center gap-4">
              <button
                type="button"
                className="btn-secondary px-4"
                onClick={() => setForm({
                  ...form,
                  guests: String(Math.max(1, parseInt(form.guests) - 1)),
                })}
              >
                −
              </button>
              <span className="text-xl font-bold w-8 text-center">{form.guests}</span>
              <button
                type="button"
                className="btn-secondary px-4"
                onClick={() => setForm({
                  ...form,
                  guests: String(parseInt(form.guests) + 1),
                })}
              >
                +
              </button>
            </div>
          </div>
        </div>

        <button type="submit" className="btn-primary w-full">
          ✅ Отправить заявку
        </button>
      </form>
    </div>
  )
}
