function navbar() {
  return (
    <nav className="Navbar">
      <div className="logo">
        QuickLink
      </div>

      <ul className="nav-links">
        <li>Home</li>

        <li>
          <a
            href="https://github.com/"
            target="_blank"
          >
            GitHub
          </a>
        </li>
      </ul>
    </nav>
  );
}

export default navbar;