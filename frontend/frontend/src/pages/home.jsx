import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import UrlForm from "../components/UrlForm";

function Home() {
  return (
    <>
      <Navbar />
      <main className="hero">
        <h1>Simplify Your Links.</h1>
        <p>A fast, secure, and professional way to shorten your URLs and track their performance.</p>
        <UrlForm />
      </main>
      <Footer />
    </>
  );
}

export default Home;