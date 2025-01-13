import Link from 'next/link';
import { useRouter } from 'next/router';

export default function Navigation() {
  const router = useRouter();
  
  const isActive = (path) => router.pathname === path;
  
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
      <div className="max-w-6xl mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link href="/">
            <a className="text-xl font-bold text-slate-800">Johnny Rapp</a>
          </Link>
          
          <div className="flex space-x-8">
            <Link href="/">
              <a className={`text-sm font-medium ${
                isActive('/') ? 'text-indigo-600' : 'text-slate-600 hover:text-slate-900'
              }`}>
                Home
              </a>
            </Link>
            
            <Link href="/about">
              <a className={`text-sm font-medium ${
                isActive('/about') ? 'text-indigo-600' : 'text-slate-600 hover:text-slate-900'
              }`}>
                About
              </a>
            </Link>
            
            <Link href="/stack">
              <a className={`text-sm font-medium ${
                isActive('/stack') ? 'text-indigo-600' : 'text-slate-600 hover:text-slate-900'
              }`}>
                Stack
              </a>
            </Link>
            
            <Link href="/connect">
              <a className="text-sm font-medium px-4 py-2 rounded-full bg-indigo-600 text-white hover:bg-indigo-700 transition-colors">
                Connect
              </a>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
} 