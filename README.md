# Real Estate Deal Analyzer

A Python-based tool for screening residential real estate deals using acquisition costs, estimated property value, and target returns.

## Why I Built It

While researching residential real estate opportunities, I was manually calculating acquisition costs, rehabilitation expenses, expected profit, and returns when screening potential deals.

I built this tool to turn that process into a repeatable analysis workflow.

## Features

- Calculates total project cost
- Estimates expected profit
- Calculates return on investment (ROI)
- Calculates the maximum purchase price for a target ROI
- Provides a simple deal assessment

## Example

For a sample deal with:

- Purchase Price: $176,000
- ARV: $246,000
- Rehabilitation: $20,000
- Closing Costs: $5,000
- Holding Costs: $3,000
- Assignment Fee: $3,000
- Target ROI: 15%

The analyzer calculates:

- Total Cost: $207,000
- Expected Profit: $39,000
- ROI: 18.84%
- Maximum Purchase Price: $182,913
- Assessment: MEETS TARGET

## How to Run

Make sure Python 3 is installed.

```bash
python main.py
```

Enter the requested deal information when prompted.

## Project Structure

```text
real-estate-deal-analyzer/
├── calculator.py
├── main.py
└── README.md
```

## Future Improvements

- Add sensitivity analysis for ARV and rehabilitation costs
- Support multiple deal scenarios
- Export analysis results
- Add a graphical interface
