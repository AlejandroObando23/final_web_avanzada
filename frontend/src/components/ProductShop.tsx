import { useState, useEffect } from "react";
import { request } from "../api/api";
import "./ProductShop.css";

interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  stock: number;
}

export default function ProductShop() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [results, setResults] = useState<Product[]>([]);
  const [searched, setSearched] = useState(false);
  
  const handleSearch = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    setLoading(true);
    setSearched(true);
    try {
      const data = await request("GET", `/projects/bf338534-365a-4d8d-b45d-1e961e182467/products?search=${query}`);
      setResults(data);
      setError(null);
    } catch (err: any) {
      setError("Error connecting to the backend");
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    handleSearch();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="mockup-wrapper">
      <h1 className="mockup-title">Products</h1>
      
      <form className="mockup-search-container" onSubmit={handleSearch}>
        <input 
          className="mockup-input" 
          placeholder="Bread" 
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit" className="mockup-button" disabled={loading}>
          {loading ? "Searching..." : "Search"}
        </button>
      </form>

      {error && (
        <div className="mockup-error">
          {error}
        </div>
      )}

      <div className="mockup-bottom-grid">
        <div className="mockup-left-panel">
          {!searched && !error && (
            <div className="mockup-left-text">
              Press Enter or click "Search" to find articles...
            </div>
          )}
          
          {searched && !error && results.length === 0 && !loading && (
             <div className="mockup-left-text">No products found.</div>
          )}
          
          {searched && !error && results.length > 0 && !loading && (
            <table className="mockup-table">
              <thead>
                <tr>
                  <th>NAME</th>
                  <th>DESCRIPTION</th>
                  <th>PRICE</th>
                  <th>STOCK</th>
                </tr>
              </thead>
              <tbody>
                {results.map((p) => (
                  <tr key={p.id}>
                    <td className="name-col">{p.name}</td>
                    <td className="desc-col">{p.description}</td>
                    <td className="price-col">${p.price.toFixed(2)}</td>
                    <td>{p.stock}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
        
        <div className="mockup-cart">
          <h2 className="mockup-cart-title">Shopping Cart</h2>
          <div className="mockup-cart-body">
            Cart is empty
          </div>
          <div className="mockup-cart-footer">
            <span className="label">Total:</span>
            <span className="amount">$0.00</span>
          </div>
        </div>
      </div>
    </div>
  );
}
