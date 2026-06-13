import { useEffect, useState } from 'react'
import './App.css'

const API_URL = 'http://localhost:8000/cars'

export default function App() {
  const [cars, setCars] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(API_URL)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error — status: ${res.status}`)
        return res.json()
      })
      .then((data) => {
        setCars(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <div className="app">
      <header className="app-header">
        <h1>🚗 Cars Directory</h1>
        <p className="subtitle">Fetched from <code>{API_URL}</code></p>
      </header>

      <main>
        {loading && (
          <div className="state-box">
            <span className="spinner" />
            <p>Loading cars…</p>
          </div>
        )}

        {error && (
          <div className="state-box error">
            <p>⚠️ Failed to load data</p>
            <small>{error}</small>
          </div>
        )}

        {!loading && !error && (
          <>
            <p className="count">{cars.length} car{cars.length !== 1 ? 's' : ''} found</p>
            <div className="grid">
              {cars.map((car) => (
                <div key={car.id} className="card">
                  <div className="card-id">#{car.id}</div>
                  <h2 className="card-name">{car.name}</h2>
                  <p className="card-model">{car.model}</p>
                  <div className="card-yom">
                    <span className="yom-label">Year</span>
                    <span className="yom-value">{car.yom}</span>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
      </main>
    </div>
  )
}
