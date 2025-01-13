import { motion } from 'framer-motion';
import Head from 'next/head';
import Image from 'next/image';

export default function About() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white">
      <Head>
        <title>About Johnny Rapp | Technology × Humanity</title>
        <meta name="description" content="Journey from meme culture pioneer to mindful tech innovator" />
      </Head>

      {/* Hero Section */}
      <section className="relative py-20 overflow-hidden">
        <div className="max-w-6xl mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center"
          >
            <div>
              <h1 className="text-4xl md:text-5xl font-bold text-slate-800 mb-6">
                Where Technology Meets Soul
              </h1>
              <p className="text-xl text-slate-600">
                I've spent my life navigating the spaces where technology and humanity collide.
              </p>
            </div>
            <div className="relative h-[400px] rounded-2xl overflow-hidden">
              <Image
                src="/profile-image.jpg"
                layout="fill"
                objectFit="cover"
                alt="Johnny Rapp"
                className="rounded-2xl"
              />
            </div>
          </motion.div>
        </div>
      </section>

      {/* Journey Timeline */}
      <section className="py-20 bg-white">
        <div className="max-w-4xl mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-slate-800 mb-12 text-center">
            The Journey
          </h2>
          
          <div className="space-y-12">
            {timelineEvents.map((event, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: index % 2 === 0 ? -20 : 20 }}
                whileInView={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.8 }}
                viewport={{ once: true }}
                className="relative pl-8 border-l-2 border-indigo-200"
              >
                <div className="absolute left-[-9px] top-0 w-4 h-4 rounded-full bg-indigo-600" />
                <div className="mb-1 text-sm text-indigo-600 font-medium">
                  {event.period}
                </div>
                <h3 className="text-xl font-bold text-slate-800 mb-2">
                  {event.title}
                </h3>
                <p className="text-slate-600">
                  {event.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Values & Philosophy */}
      <section className="py-20 bg-slate-50">
        <div className="max-w-6xl mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-slate-800 mb-12 text-center">
            Values & Philosophy
          </h2>
          
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8"
          >
            {values.map((value, index) => (
              <div key={index} className="bg-white p-8 rounded-2xl shadow-sm">
                <div className="text-3xl text-indigo-600 mb-4">
                  {value.icon}
                </div>
                <h3 className="text-xl font-bold text-slate-800 mb-2">
                  {value.title}
                </h3>
                <p className="text-slate-600">
                  {value.description}
                </p>
              </div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Current Focus */}
      <section className="py-20 bg-white">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
          >
            <h2 className="text-3xl md:text-4xl font-bold text-slate-800 mb-6">
              Current Focus
            </h2>
            <p className="text-xl text-slate-600 mb-8">
              Today, I focus on the connection—where humanity meets creativity, and where innovation 
              can actually make us more human. Through projects like JRAPP Media, Symphony, and 
              producing films with Cuneiform, I explore how technology is reshaping our world—on 
              the main stage, in small towns, and in the spaces in between.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {currentProjects.map((project, index) => (
                <div key={index} className="p-6 bg-slate-50 rounded-2xl">
                  <h3 className="text-xl font-bold text-slate-800 mb-2">
                    {project.name}
                  </h3>
                  <p className="text-slate-600">
                    {project.description}
                  </p>
                </div>
              ))}
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}

const timelineEvents = [
  {
    period: "Early Days",
    title: "Social Media Pioneer",
    description: "Started in the early days of social media, crafting a voice in the chaos and helping shape what we now call meme culture. Built a network reaching millions."
  },
  {
    period: "Growth Phase",
    title: "Digital Marketing Evolution",
    description: "Worked with brands, artists, and festivals to create stories that people actually cared about. Developed expertise in authentic digital connection."
  },
  {
    period: "Transformation",
    title: "Spiritual Awakening",
    description: "Discovered the deeper potential of technology to foster genuine human connection and spiritual growth. Began integrating mindfulness with digital innovation."
  },
  {
    period: "Present",
    title: "Bridge Builder",
    description: "Creating spaces where technology enhances rather than replaces human connection. Helping others navigate the intersection of digital progress and personal growth."
  }
];

const values = [
  {
    icon: "🌱",
    title: "Personal Evolution",
    description: "Dedicated to continuous growth of mind, body, and spirit. Embracing change and transformation."
  },
  {
    icon: "🌍",
    title: "Adventure & Discovery",
    description: "Pursuing daily adventures and new experiences. Embracing geographical and cultural exploration."
  },
  {
    icon: "✨",
    title: "Optimistic Faith",
    description: "Maintaining hope and positive outlook. Finding meaning through spiritual connection."
  },
  {
    icon: "🤖",
    title: "Conscious Technology",
    description: "Using technology as a tool for enhancement, not replacement. Balancing digital innovation with human connection."
  }
];

const currentProjects = [
  {
    name: "JRAPP Media",
    description: "Service-based company focusing on impactful partnerships and authentic digital presence."
  },
  {
    name: "Symphony",
    description: "Pioneering AI-driven advertising solutions that maintain human connection at their core."
  },
  {
    name: "Film Production",
    description: "Collaborating with Cuneiform to tell stories that bridge technology and humanity."
  }
]; 