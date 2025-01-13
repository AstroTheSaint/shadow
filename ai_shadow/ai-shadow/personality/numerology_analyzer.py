"""
Numerology Analyzer
Calculates and interprets numerological significance using Pythagorean system
"""

from datetime import datetime
from typing import Dict, List, Tuple
import re

class NumerologyAnalyzer:
    def __init__(self):
        self.pythagorean_chart = {
            'A': 1, 'J': 1, 'S': 1,
            'B': 2, 'K': 2, 'T': 2,
            'C': 3, 'L': 3, 'U': 3,
            'D': 4, 'M': 4, 'V': 4,
            'E': 5, 'N': 5, 'W': 5,
            'F': 6, 'O': 6, 'X': 6,
            'G': 7, 'P': 7, 'Y': 7,
            'H': 8, 'Q': 8, 'Z': 8,
            'I': 9, 'R': 9
        }
        
        self.master_numbers = {11, 22, 33}
        
    def analyze_full_profile(self, name: str, birth_date: datetime) -> Dict:
        """Calculate complete numerological profile"""
        
        # Core numbers
        life_path = self.calculate_life_path(birth_date)
        destiny = self.calculate_destiny_number(name)
        soul_urge = self.calculate_soul_urge(name)
        personality = self.calculate_personality_number(name)
        expression = self.calculate_expression_number(name)
        
        # Birth date numbers
        birth_day = self.calculate_birth_day_number(birth_date)
        
        # Cycles and pinnacles
        cycles = self.calculate_life_cycles(birth_date)
        pinnacles = self.calculate_pinnacles(name, birth_date)
        
        # Personal years and months
        current_year = self.calculate_personal_year(birth_date)
        current_month = self.calculate_personal_month(birth_date)
        
        return {
            'core_numbers': {
                'life_path': {
                    'number': life_path,
                    'meaning': self.interpret_life_path(life_path)
                },
                'destiny': {
                    'number': destiny,
                    'meaning': self.interpret_destiny(destiny)
                },
                'soul_urge': {
                    'number': soul_urge,
                    'meaning': self.interpret_soul_urge(soul_urge)
                },
                'personality': {
                    'number': personality,
                    'meaning': self.interpret_personality(personality)
                },
                'expression': {
                    'number': expression,
                    'meaning': self.interpret_expression(expression)
                }
            },
            'birth_day': {
                'number': birth_day,
                'meaning': self.interpret_birth_day(birth_day)
            },
            'cycles': {
                'data': cycles,
                'interpretation': self.interpret_cycles(cycles)
            },
            'pinnacles': {
                'data': pinnacles,
                'interpretation': self.interpret_pinnacles(pinnacles)
            },
            'current': {
                'year': {
                    'number': current_year,
                    'meaning': self.interpret_personal_year(current_year)
                },
                'month': {
                    'number': current_month,
                    'meaning': self.interpret_personal_month(current_month)
                }
            }
        }
        
    def calculate_life_path(self, birth_date: datetime) -> int:
        """Calculate Life Path Number"""
        date_str = birth_date.strftime('%Y%m%d')
        return self._reduce_to_single_digit(sum(int(d) for d in date_str))
        
    def calculate_destiny_number(self, name: str) -> int:
        """Calculate Destiny/Expression Number"""
        total = sum(self.pythagorean_chart.get(c.upper(), 0) for c in name if c.isalpha())
        return self._reduce_to_single_digit(total)
        
    def calculate_soul_urge(self, name: str) -> int:
        """Calculate Soul Urge/Heart's Desire Number"""
        vowels = 'AEIOU'
        total = sum(self.pythagorean_chart.get(c.upper(), 0) 
                   for c in name if c.upper() in vowels)
        return self._reduce_to_single_digit(total)
        
    def calculate_personality_number(self, name: str) -> int:
        """Calculate Personality Number"""
        consonants = ''.join(c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if c not in 'AEIOU')
        total = sum(self.pythagorean_chart.get(c.upper(), 0) 
                   for c in name if c.upper() in consonants)
        return self._reduce_to_single_digit(total)
        
    def calculate_expression_number(self, name: str) -> int:
        """Calculate Expression Number"""
        return self.calculate_destiny_number(name)  # Same as destiny number
        
    def calculate_birth_day_number(self, birth_date: datetime) -> int:
        """Calculate Birth Day Number"""
        return self._reduce_to_single_digit(birth_date.day)
        
    def calculate_life_cycles(self, birth_date: datetime) -> List[Dict]:
        """Calculate Life Cycles"""
        month = self._reduce_to_single_digit(birth_date.month)
        day = self._reduce_to_single_digit(birth_date.day)
        year = self._reduce_to_single_digit(birth_date.year)
        
        return [
            {'cycle': 1, 'number': month, 'age_range': '0-28'},
            {'cycle': 2, 'number': day, 'age_range': '29-56'},
            {'cycle': 3, 'number': year, 'age_range': '57+'}
        ]
        
    def calculate_pinnacles(self, name: str, birth_date: datetime) -> List[Dict]:
        """Calculate Pinnacle Numbers"""
        # Implementation of pinnacle calculations
        return []  # Placeholder
        
    def calculate_personal_year(self, birth_date: datetime) -> int:
        """Calculate Personal Year Number"""
        current_year = datetime.now().year
        month_day = birth_date.strftime('%m%d')
        return self._reduce_to_single_digit(
            sum(int(d) for d in f"{current_year}{month_day}")
        )
        
    def calculate_personal_month(self, birth_date: datetime) -> int:
        """Calculate Personal Month Number"""
        personal_year = self.calculate_personal_year(birth_date)
        current_month = datetime.now().month
        return self._reduce_to_single_digit(personal_year + current_month)
        
    def _reduce_to_single_digit(self, number: int) -> int:
        """Reduce number to single digit unless it's a master number"""
        if number in self.master_numbers:
            return number
            
        while number > 9:
            number = sum(int(d) for d in str(number))
        return number
        
    def interpret_life_path(self, number: int) -> str:
        """Interpret Life Path Number"""
        interpretations = {
            1: "Natural born leader, independent, innovative",
            2: "Diplomatic, cooperative, sensitive to others",
            3: "Creative, expressive, optimistic",
            4: "Practical, organized, stable",
            5: "Adventurous, versatile, freedom-loving",
            6: "Responsible, caring, harmonious",
            7: "Analytical, spiritual, seeking wisdom",
            8: "Ambitious, material success, power",
            9: "Humanitarian, compassionate, universal",
            11: "Spiritual messenger, intuitive, illumination",
            22: "Master builder, practical idealist, potential for achievement",
            33: "Master teacher, nurturing, spiritual understanding"
        }
        return interpretations.get(number, "Unknown number")
        
    # Additional interpretation methods for other numbers...
    def interpret_destiny(self, number: int) -> str:
        """Interpret Destiny Number"""
        return "Destiny interpretation placeholder"
        
    def interpret_soul_urge(self, number: int) -> str:
        """Interpret Soul Urge Number"""
        return "Soul Urge interpretation placeholder"
        
    def interpret_personality(self, number: int) -> str:
        """Interpret Personality Number"""
        return "Personality interpretation placeholder"
        
    def interpret_expression(self, number: int) -> str:
        """Interpret Expression Number"""
        return "Expression interpretation placeholder"
        
    def interpret_birth_day(self, number: int) -> str:
        """Interpret Birth Day Number"""
        return "Birth Day interpretation placeholder"
        
    def interpret_cycles(self, cycles: List[Dict]) -> str:
        """Interpret Life Cycles"""
        return "Cycles interpretation placeholder"
        
    def interpret_pinnacles(self, pinnacles: List[Dict]) -> str:
        """Interpret Pinnacles"""
        return "Pinnacles interpretation placeholder"
        
    def interpret_personal_year(self, number: int) -> str:
        """Interpret Personal Year Number"""
        return "Personal Year interpretation placeholder"
        
    def interpret_personal_month(self, number: int) -> str:
        """Interpret Personal Month Number"""
        return "Personal Month interpretation placeholder" 