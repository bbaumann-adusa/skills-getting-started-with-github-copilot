document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");

  // Function to fetch activities from API
  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      // Clear loading message
      activitiesList.innerHTML = "";

      // Populate activities list
      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - details.participants.length;

        activityCard.innerHTML = `
          <h4>${name}</h4>
          <p>${details.description}</p>
          <p><strong>Schedule:</strong> ${details.schedule}</p>
          <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
        `;

        activitiesList.appendChild(activityCard);

        // Add option to select dropdown
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        activitySelect.appendChild(option);
      });
    } catch (error) {
      activitiesList.innerHTML = "<p>Failed to load activities. Please try again later.</p>";
      console.error("Error fetching activities:", error);
    }
  }

  // Handle form submission
  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const activity = document.getElementById("activity").value;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}`,
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        messageDiv.textContent = result.message;
        messageDiv.className = "success";
        signupForm.reset();
      } else {
        messageDiv.textContent = result.detail || "An error occurred";
        messageDiv.className = "error";
      }

      messageDiv.classList.remove("hidden");

      // Hide message after 5 seconds
      setTimeout(() => {
        messageDiv.classList.add("hidden");
      }, 5000);
    } catch (error) {
      messageDiv.textContent = "Failed to sign up. Please try again.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
      console.error("Error signing up:", error);
    }
  });

  // Function to fetch and render the daily Last Mile news report
  async function fetchNewsReport() {
    const newsDate = document.getElementById("news-date");
    const newsSummary = document.getElementById("news-summary");
    const newsList = document.getElementById("news-list");

    try {
      const response = await fetch("/news/daily");
      const report = await response.json();

      newsDate.textContent = `Report Date: ${report.report_date}`;
      newsSummary.textContent = report.summary;
      newsSummary.classList.remove("hidden");

      newsList.innerHTML = "";

      report.competitors.forEach((competitor) => {
        const card = document.createElement("div");
        card.className = "news-card";

        const focusTags = competitor.focus_areas
          .map((area) => `<span class="focus-tag">${area}</span>`)
          .join(" ");

        const highlights = competitor.last_mile_highlights
          .map((h) => `<li>${h}</li>`)
          .join("");

        card.innerHTML = `
          <h4>${competitor.name}</h4>
          <p class="competitor-desc">${competitor.description}</p>
          <div class="focus-tags">${focusTags}</div>
          <ul class="highlights-list">${highlights}</ul>
        `;

        newsList.appendChild(card);
      });
    } catch (error) {
      newsDate.textContent = "Failed to load news report. Please try again later.";
      console.error("Error fetching news report:", error);
    }
  }

  // Initialize app
  fetchActivities();
  fetchNewsReport();
});
