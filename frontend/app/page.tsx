"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState<string | null>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/hello`)
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      });
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1>Welcome to the Home Page</h1>
      <p>{message || "Loading..."}</p>
    </div>
  );
}