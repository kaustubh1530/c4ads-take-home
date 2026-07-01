import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [entities, setEntities] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [country, setCountry] = useState('')
  const [entityType, setEntityType] = useState('')

  useEffect(() => {
    fetchEntities()
  }, [country, entityType])

  const fetchEntities = async () => {
    setLoading(true)
    setError(null)
    try {
      const params = new URLSearchParams()
      if (country) params.append('country', country)
      if (entityType) params.append('entity_type', entityType)

      const res = await fetch(`/api/entities/?${params.toString()}`)
      if (!res.ok) throw new Error(`HTTP error: ${res.status}`)
      const data = await res.json()
      setEntities(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const countries = [
    '', 'Russia', 'China', 'Iran', 'North Korea', 'UAE', 'Turkey',
    'Venezuela', 'Syria', 'Ukraine', 'Cyprus', 'Singapore', 'Germany',
    'Malta', 'Panama', 'Switzerland', 'Luxembourg', 'Serbia', 'Kazakhstan',
    'Lebanon', 'Iraq', 'Somalia', 'Ghana', 'Kuwait', 'Saudi Arabia',
    'Bolivia', 'Colombia', 'Mexico', 'Peru', 'Brazil', 'Japan', 'Taiwan',
    'Philippines', 'Malaysia', 'Hong Kong', 'Oman', 'Georgia', 'Azerbaijan',
    'Estonia', 'Netherlands', 'Spain', 'Italy', 'Greece', 'Liberia',
    'Togo', 'Senegal', 'Kenya', 'Yemen', 'Tunisia', 'Canada', 'Australia',
    'British Virgin Islands', 'Cayman Islands', 'Isle of Man', 'Monaco',
    'Marshall Islands', 'Czech Republic'
  ]

  return (
    <div className="container">
      <h1>C4ADS Sanctioned Entities</h1>

      <div className="filters">
        <div className="filter-group">
          <label>Country</label>
          <select value={country} onChange={e => setCountry(e.target.value)}>
            <option value="">All Countries</option>
            {countries.filter(c => c).sort().map(c => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
          {country && <span className="active-filter">✓ {country}</span>}
        </div>

        <div className="filter-group">
          <label>Entity Type</label>
          <select value={entityType} onChange={e => setEntityType(e.target.value)}>
            <option value="">All Types</option>
            <option value="Individual">Individual</option>
            <option value="Organization">Organization</option>
          </select>
          {entityType && <span className="active-filter">✓ {entityType}</span>}
        </div>

        <div className="filter-group">
          <label>&nbsp;</label>
          <button onClick={() => { setCountry(''); setEntityType('') }}>
            Clear Filters
          </button>
        </div>
      </div>

      {(country || entityType) && (
        <div className="active-filters-bar">
          <span>Filtering by:</span>
          {country && <span className="tag">{country}</span>}
          {entityType && <span className="tag">{entityType}</span>}
        </div>
      )}

      {loading && <p className="status">Loading...</p>}
      {error && <p className="status error">Error: {error}</p>}
      {!loading && !error && (
        <>
          <p className="count">{entities.length} result{entities.length !== 1 ? 's' : ''}</p>
          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Country</th>
                  <th>Type</th>
                  <th>Date Added</th>
                  <th>Program</th>
                </tr>
              </thead>
              <tbody>
                {entities.length === 0 ? (
                  <tr><td colSpan="5" className="no-results">No results found.</td></tr>
                ) : (
                  entities.map(e => (
                    <tr key={e.id}>
                      <td>{e.name}</td>
                      <td>{e.country}</td>
                      <td>
                        <span className={`badge ${e.entity_type === 'Individual' ? 'badge-individual' : 'badge-org'}`}>
                          {e.entity_type}
                        </span>
                      </td>
                      <td>{e.date_added}</td>
                      <td>{e.program}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  )
}
export default App