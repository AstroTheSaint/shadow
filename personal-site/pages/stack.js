import { motion } from 'framer-motion';
import Head from 'next/head';

export default function Stack() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white">
      <Head>
        <title>Tech Stack | Johnny Rapp</title>
        <meta name="description" content="Tools and technologies I use to create impact" />
      </Head>

      {/* Hero Section */}
      <section className="py-20">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h1 className="text-4xl md:text-5xl font-bold text-slate-800 mb-6">
              My Digital Toolbox
            </h1>
            <p className="text-xl text-slate-600">
              These are the tools and technologies I use to create impact and foster connection.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Stack Categories */}
      <section className="py-20">
        <div className="max-w-6xl mx-auto px-4">
          {categories.map((category, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: index * 0.1 }}
              viewport={{ once: true }}
              className="mb-16 last:mb-0"
            >
              <h2 className="text-2xl md:text-3xl font-bold text-slate-800 mb-8">
                {category.name}
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {category.tools.map((tool, toolIndex) => (
                  <div
                    key={toolIndex}
                    className="bg-white p-6 rounded-2xl shadow-sm hover:shadow-md transition-shadow"
                  >
                    <div className="flex items-start space-x-4">
                      <div className="flex-shrink-0 w-12 h-12 flex items-center justify-center bg-indigo-100 rounded-xl">
                        {tool.icon}
                      </div>
                      <div>
                        <h3 className="text-lg font-bold text-slate-800 mb-2">
                          {tool.name}
                        </h3>
                        <p className="text-slate-600 text-sm">
                          {tool.description}
                        </p>
                        {tool.useCase && (
                          <div className="mt-2 text-sm">
                            <span className="text-indigo-600 font-medium">Use case: </span>
                            <span className="text-slate-600">{tool.useCase}</span>
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Philosophy Section */}
      <section className="py-20 bg-slate-50">
        <div className="max-w-4xl mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="text-center"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-slate-800 mb-6">
              Tool Philosophy
            </h2>
            <p className="text-xl text-slate-600">
              Every tool in my stack is chosen with intention. It's not just about what's new or 
              trendy—it's about what genuinely enhances human connection and creates meaningful impact.
            </p>
          </motion.div>
        </div>
      </section>
    </div>
  );
}

const categories = [
  {
    name: "Creation & Design",
    tools: [
      {
        name: "Adobe Creative Suite",
        icon: "🎨",
        description: "Full creative suite for visual storytelling and brand development.",
        useCase: "Creating impactful visual narratives and brand identities"
      },
      {
        name: "Figma",
        icon: "✏️",
        description: "Collaborative design tool for web and mobile interfaces.",
        useCase: "Designing user-centered digital experiences"
      },
      {
        name: "Canva",
        icon: "🖼️",
        description: "Quick, beautiful design creation for social media and marketing.",
        useCase: "Rapid content creation and social media assets"
      }
    ]
  },
  {
    name: "Development & Technology",
    tools: [
      {
        name: "Next.js",
        icon: "⚡",
        description: "React framework for production-grade web applications.",
        useCase: "Building fast, SEO-friendly web experiences"
      },
      {
        name: "TailwindCSS",
        icon: "🎯",
        description: "Utility-first CSS framework for rapid styling.",
        useCase: "Creating beautiful, responsive interfaces"
      },
      {
        name: "Claude & GPT-4",
        icon: "🤖",
        description: "Advanced AI models for content and strategy.",
        useCase: "AI-powered content creation and analysis"
      }
    ]
  },
  {
    name: "Productivity & Organization",
    tools: [
      {
        name: "Notion",
        icon: "📝",
        description: "All-in-one workspace for notes, projects, and collaboration.",
        useCase: "Project management and content organization"
      },
      {
        name: "Superhuman",
        icon: "✉️",
        description: "The fastest email experience ever made.",
        useCase: "Efficient email management and communication"
      },
      {
        name: "Calendly",
        icon: "📅",
        description: "Automated scheduling and booking system.",
        useCase: "Streamlined meeting coordination"
      }
    ]
  },
  {
    name: "Content & Social",
    tools: [
      {
        name: "Later",
        icon: "📱",
        description: "Social media scheduling and analytics platform.",
        useCase: "Strategic content planning and posting"
      },
      {
        name: "Descript",
        icon: "🎬",
        description: "All-in-one audio/video editing and transcription.",
        useCase: "Creating engaging video content"
      },
      {
        name: "Riverside",
        icon: "🎙️",
        description: "Professional remote recording platform.",
        useCase: "High-quality podcast and video recording"
      }
    ]
  },
  {
    name: "Mindfulness & Wellness",
    tools: [
      {
        name: "Headspace",
        icon: "🧘‍♂️",
        description: "Guided meditation and mindfulness app.",
        useCase: "Daily meditation and mental clarity"
      },
      {
        name: "Day One",
        icon: "📔",
        description: "Digital journaling app for reflection.",
        useCase: "Personal reflection and gratitude practice"
      },
      {
        name: "Focus@Will",
        icon: "🎵",
        description: "Productivity music backed by neuroscience.",
        useCase: "Enhanced focus and concentration"
      }
    ]
  }
]; 