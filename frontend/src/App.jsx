import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import Home from "./pages/Home";
import Performances from "./pages/Performances";
import AskKala from "./pages/AskKala";
import Revival from "./pages/Revival";

function Navbar() {
  const link = "px-3 py-2 rounded-lg hover:bg-brand-bg/80 transition";
  const active = "bg-brand-brown text-white hover:bg-brand-brown/90";
  return (
    <header className="border-b bg-brand-bg">
      <div className="max-w-5xl mx-auto px-4 py-6 text-center">
        {/* Text logo */}
        <div className="text-3xl font-heading font-bold tracking-wide">
          Kala
        </div>
        {/* Subtle underline accent */}
        <div className="mx-auto mt-2 h-1 w-16 rounded-full bg-brand-green" />
        {/* Centered nav */}
        <nav className="mt-4 flex justify-center gap-2">
          <NavLink to="/" end className={({isActive}) => `${link} ${isActive?active:""}`}>Home</NavLink>
          <NavLink to="/performances" className={({isActive}) => `${link} ${isActive?active:""}`}>Performances</NavLink>
          <NavLink to="/ask" className={({isActive}) => `${link} ${isActive?active:""}`}>Ask Kala</NavLink>
          <NavLink to="/revival" className={({isActive}) => `${link} ${isActive?active:""}`}>Revival</NavLink>
        </nav>
      </div>
    </header>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-1 p-6 max-w-5xl mx-auto w-full">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/performances" element={<Performances />} />
            <Route path="/ask" element={<AskKala />} />
            <Route path="/revival" element={<Revival />} />
          </Routes>
        </main>
        <footer className="p-6 text-center text-sm text-brand-brown/70 border-t">
          © Kala — Performance • Knowledge • Revival
        </footer>
      </div>
    </BrowserRouter>
  );
}
