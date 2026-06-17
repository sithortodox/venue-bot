import { Link, useParams } from 'react-router-dom'

const eventsData: Record<string, {
  title: string
  date: string
  venue: string
  price: string
  description: string
}> = {
  '1': {
    title: 'Night Party',
    date: '21 июня, 21:00 - 05:00',
    venue: 'Main Hall',
    price: 'от 1500₽',
    description: 'Лучшая вечеринка города! DJ-сет, коктейли, атмосфера. Не пропустите главную ночь недели!',
  },
  '2': {
    title: 'Lounge Evening',
    date: '23 июня, 20:00 - 02:00',
    venue: 'Terrace',
    price: 'от 1000₽',
    description: 'Спокойный вечер в lounge-зоне. Живая музыка, крафтовые напитки, уютная атмосфера.',
  },
  '3': {
    title: 'VIP Night',
    date: '25 июня, 21:00 - 04:00',
    venue: 'VIP Zone',
    price: 'от 3000₽',
    description: 'Эксклюзивное мероприятие для VIP-гостей. Ограниченное количество мест, персональный сервис.',
  },
  '4': {
    title: 'Rooftop Sunset',
    date: '28 июня, 19:00 - 01:00',
    venue: 'Rooftop',
    price: 'от 2000₽',
    description: 'Встречаем закат на крыше. Коктейли, закуски, живая атмосфера и потрясающий вид на город.',
  },
}

export default function EventDetail() {
  const { id } = useParams()
  const event = eventsData[id || '1']

  if (!event) {
    return (
      <div className="p-4 text-center">
        <p>Мероприятие не найдено</p>
        <Link to="/events" className="btn-primary inline-block mt-4">К афише</Link>
      </div>
    )
  }

  return (
    <div className="p-4 space-y-4">
      <header className="flex items-center justify-between">
        <Link to="/events" className="text-white/60">← Назад</Link>
        <h1 className="text-xl font-bold">{event.title}</h1>
        <div className="w-10" />
      </header>

      <div className="card">
        <div className="aspect-video bg-white/5 rounded-xl flex items-center justify-center">
          <span className="text-6xl">🎭</span>
        </div>
      </div>

      <div className="card space-y-3">
        <div>
          <p className="text-white/60 text-sm">Дата и время</p>
          <p className="font-medium">{event.date}</p>
        </div>
        <div>
          <p className="text-white/60 text-sm">Площадка</p>
          <p className="font-medium">{event.venue}</p>
        </div>
        <div>
          <p className="text-white/60 text-sm">Цена</p>
          <p className="font-medium text-primary">{event.price}</p>
        </div>
        <div>
          <p className="text-white/60 text-sm">Описание</p>
          <p className="font-medium">{event.description}</p>
        </div>
      </div>

      <div className="space-y-2">
        <Link to="/booking" className="btn-primary block text-center">
          📞 Забронировать стол
        </Link>
        <a
          href="https://t.me/venue_admin"
          className="btn-secondary block text-center"
        >
          💬 Связаться с админом
        </a>
      </div>
    </div>
  )
}
