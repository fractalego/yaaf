"use client"

import * as React from "react"

function ReviewerAgent(element: { text: string }) {
  return (
    <div className="inline-block bg-pink-100 p-3 text-xl rounded-sm">
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
          className="lucide lucide-search-check-icon lucide-search-check"
        >
          <path d="m8 11 2 2 4-4" />
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.3-4.3" />
        </svg>
      </div>
      {element.text}
    </div>
  )
}

ReviewerAgent.displayName = "ReviewerAgent"
export { ReviewerAgent }
