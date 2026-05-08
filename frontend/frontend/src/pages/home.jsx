import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

function Home() {
  return (
    <>
      <Navbar />

      <main className="hero">
        <h1>
          Shorten Your URLs Instantly
        </h1>

        <p>
          Clean. Fast. Simple URL shortening.
        </p>
      </main>

      <Footer />
    </>
  );
}

export default Home;