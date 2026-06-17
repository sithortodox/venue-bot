import { Link } from 'react-router-dom'

const events = [
  {
    id: 1,
    title: 'Night Party',
    date: '21 июня, 21:00',
    venue: 'Main Hall',
    price: 'от 1500₽',
    description: 'Лучшая вечеринка города!',
  },
  {
    id: 2,
    title: 'Lounge Evening',
    date: '23 июня, 20:00',
    venue: 'Terrace',
    price: 'от 1000₽',
    description: 'Спокойный вечер в lounge-зоне',
  },
  {
    id: 3,
    title: 'VIP Night',
    date: '25 июня, 21:00',
    venue: 'VIP Zone',
    price: 'от 3000₽',
    description: 'Эксклюзивное VIP-мероприятие',
  },
  {
    id: 4,
    title: 'Rooftop Sunset',
    date: '28 июня, 19:00',
    venue: 'Rooftop',
    price: 'от 2000₽',
    description: 'Встречаем закат на крыше',
  },
]

export default function Events() {
  return (
    <div className="p-4 space-y-4">
      <header className="flex items-center justify-between">
        <Link to="/" className="text-white/60">← Назад</Link>
        <h1 className="text-xl font-bold">Афиша</h1>
        <div className="w-10" />
      </header>

      <div className="space-y-3">
        {events.map((event) => (
          <Link
            key={event.id}
            to={`/events/${event.id}`}
            className="card block"
          >
            <div className="flex justify-between items-start">
              <div>
                <h2 className="font-bold text-lg">{event.title}</h2>
                <p className="text-white/60 text-sm mt-1">{event.date}</p>
                <p className="text-white/60 text-sm">{event.venue}</p>
              </div>
              <span className="text-primary font-bold">{event.price}</span>
            </div>
            <p className="text-white/80 mt-2 text-sm">{event.description}</p>
          </Link>
        ))}
      </div>
    </div>
  )
}
