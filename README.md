# ReviewScheduler

**ReviewScheduler** is a utility program for generating and managing review schedules based on fixed intervals. It focuses only on dates, making it suitable for use alongside other learning or review systems.

---

## Features

* Generates a structured review schedule based on a predefined table of intervals.
* Produces two main JSON files:

  * `daily.json`: Maps each learning date to its scheduled review dates.
  * `reviews_by_date.json`: Maps each review date to the learning dates due on that day.

* Creates a `today.md` file with daily review requirements, organized by priority.
* Archives past `today.md` files into a `history/` directory for record-keeping.
* Automatically maintains backups of schedule files for reliability.

---

## Review Intervals

For each learning date (**D0**), the following review dates are generated:

| Review Step | Review Day | Offset from D0    |
| ----------- | ---------- | ----------------- |
| Initial     | Day 1      | D0 (learning day) |
| 2           | Day 3      | +2 days           |
| 3           | Day 7      | +6 days           |
| 4           | Day 14     | +13 days          |
| 5           | Day 30     | +29 days          |
| 6           | Day 60     | +59 days          |
| 7           | Day 120    | +119 days         |

---

## Directory Structure

* `schedule/`: Generated scheduling files (`daily.json` and `review_by_date.json`).
* `history/`: Archived daily review files.
* `schedule/backup/`: Backups of core schedule files.

---

## Example `today.md`

```markdown
# 2025-08-08

## Top Priority Reviews

*Reviews scheduled for 2 and 6 days after learning.*

+ 2025-08-06
+ 2025-08-02

## Middle Priority Reviews

*Reviews scheduled for 13 and 29 days after learning.*

+ 2025-08-01
+ 2025-07-24

## Least Priority Reviews

*Reviews scheduled for 59 and 119 days after learning.*

+ 2025-07-09
```

---

## Future Features

* **Missed Days and Overdue Handling**

  * Automatically detect and reschedule missed reviews.

* **Daily Caps**

  * Limit the number of reviews per day and redistribute lower-priority items.

---

## License

This project is licensed under the [MIT License](LICENSE).

---
