import { motion } from 'framer-motion';
import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white">
      <Head>
        <title>Johnny Rapp | Technology × Humanity</title>
        <meta name="description" content="Helping you thrive where humanity meets technology" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* Hero Section */}
      <motion.section 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="relative h-screen flex items-center justify-center overflow-hidden"
      >
        <div className="absolute inset-0 z-0">
          <video
            autoPlay
            loop
            muted
            playsInline
            className="object-cover w-full h-full opacity-30"
          >
            <source src="/hero-background.mp4" type="video/mp4" />
          </video>
        </div>

        <div className="relative z-10 max-w-4xl mx-auto px-4 text-center">
          <motion.h1 
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-5xl md:text-7xl font-bold text-slate-800 mb-6"
          >
            Humanity meets technology
          </motion.h1>
          <motion.p 
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="text-xl md:text-2xl text-slate-600 mb-8"
          >
            Guidance, tools, and stories to inspire creativity and connection in a chaotic world.
          </motion.p>
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.6 }}
          >
            <Link href="/connect">
              <a className="inline-block bg-indigo-600 text-white px-8 py-4 rounded-full text-lg font-medium hover:bg-indigo-700 transition-colors">
                Begin Your Journey
              </a>
            </Link>
          </motion.div>
        </div>

        <motion.div 
          initial={{ y: 50, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.8 }}
          className="absolute bottom-10 left-1/2 transform -translate-x-1/2"
        >
          <div className="animate-bounce">
            <svg className="w-6 h-6 text-slate-600" fill="none" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
            </svg>
          </div>
        </motion.div>
      </motion.section>

      {/* Manifesto Section */}
      <section className="py-20 bg-white">
        <div className="max-w-4xl mx-auto px-4">
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="prose prose-lg"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-slate-800 mb-8">
              The world is loud. Too loud, sometimes.
            </h2>
            <p className="text-slate-600">
              There's this constant hum—a barrage of notifications, deadlines, and the endless chase for "what's next." 
              It's easy to get lost in it all, to forget the things that actually matter.
            </p>
            <p className="text-slate-600">
              But you're not here to keep up. You're here to create, to connect, to build something meaningful. 
              That's what I'm here for: to help you cut through the noise, rediscover what's real, and create 
              a life that's as extraordinary as it is impactful.
            </p>
            <p className="text-slate-600 font-medium">
              It starts with one step. Let's take it together.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Services Grid */}
      <section className="py-20 bg-slate-50">
        <div className="max-w-6xl mx-auto px-4">
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="grid grid-cols-1 md:grid-cols-3 gap-8"
          >
            {/* Mindfulness Card */}
            <div className="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
              <h3 className="text-2xl font-bold text-slate-800 mb-4">Mindfulness</h3>
              <p className="text-slate-600">
                Find your center. Life moves fast, but the good stuff doesn't happen when you're rushing. 
                Through meditation, gratitude practices, and breathwork, I'll help you slow down and reconnect with yourself.
              </p>
            </div>

            {/* Creativity Card */}
            <div className="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
              <h3 className="text-2xl font-bold text-slate-800 mb-4">Creativity</h3>
              <p className="text-slate-600">
                Build your story. Whether you're an entrepreneur, a creator, or someone with a vision, 
                I'll help you unlock your unique voice and use it to make an impact—online, offline, anywhere.
              </p>
            </div>

            {/* Innovation Card */}
            <div className="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
              <h3 className="text-2xl font-bold text-slate-800 mb-4">Innovation</h3>
              <p className="text-slate-600">
                Step into the future. From AI-driven strategies to crafting stories through film, 
                I'll show you how to harness technology without losing what makes you human.
              </p>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-20 bg-white">
        <div className="max-w-6xl mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-slate-800 mb-12 text-center">
            What Others Are Saying
          </h2>
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="grid grid-cols-1 md:grid-cols-3 gap-8"
          >
            {testimonials.map((testimonial, index) => (
              <div key={index} className="bg-slate-50 p-8 rounded-2xl">
                <p className="text-slate-600 mb-6 italic">"{testimonial.quote}"</p>
                <p className="font-medium text-slate-800">— {testimonial.author}</p>
              </div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-indigo-600">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
          >
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
              Begin Your Journey Today
            </h2>
            <p className="text-indigo-100 mb-8">
              The world is loud, but your story deserves to be heard. Let's create something meaningful—together.
            </p>
            <Link href="/connect">
              <a className="inline-block bg-white text-indigo-600 px-8 py-4 rounded-full text-lg font-medium hover:bg-indigo-50 transition-colors">
                Start Your New Digital Life
              </a>
            </Link>
          </motion.div>
        </div>
      </section>
    </div>
  );
}

const testimonials = [
  {
    quote: "Johnny has this way of making technology feel… human. Working with him didn't just grow my business—it helped me connect with people in ways I never thought possible.",
    author: "Marcus N."
  },
  {
    quote: "His insights go beyond the surface. Johnny helped me rethink not just what I do, but how I live. It's been a game-changer.",
    author: "Arielle G."
  },
  {
    quote: "He blends creativity, mindfulness, and innovation in a way that's rare. Johnny doesn't just talk about connection—he creates it.",
    author: "Gary S."
  }
]; 