import ProductShop from './components/ProductShop'
import './index.css'

function App() {
  return (
    <div style={{ backgroundColor: '#080808', minHeight: '100vh', padding: '20px' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <ProductShop />
      </div>
    </div>
  )
}

export default App
