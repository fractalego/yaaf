"use client"

import * as React from "react"

function VisualizationAgent(element: { text: string }) {
  return (
    <div className="inline-block bg-indigo-100 p-3 text-xl rounded-sm">
      <div className="inline-block pr-5">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          className="lucide lucide-chart-candlestick-icon lucide-chart-candlestick"
        >
          <path d="M9 5v4" />
          <rect width="4" height="6" x="7" y="9" rx="1" />
          <path d="M9 15v2" />
          <path d="M17 3v2" />
          <rect width="4" height="8" x="15" y="5" rx="1" />
          <path d="M17 13v3" />
          <path d="M3 3v16a2 2 0 0 0 2 2h16" />
        </svg>
      </div>
      {element.text}
    </div>
  )
}

VisualizationAgent.displayName = "VisualizationAgent"
export { VisualizationAgent }
