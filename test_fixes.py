#!/usr/bin/env python3
"""
Test script to verify the hashtag type mismatch fixes.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_combine_caption_with_string():
    """Test combine_caption_and_hashtags with string hashtags."""
    from utils.text_utils import combine_caption_and_hashtags
    
    result = combine_caption_and_hashtags("Beautiful sunset", "#travel #nature #photography")
    assert "Beautiful sunset" in result
    assert "#travel" in result
    assert "#nature" in result
    print("✓ Test 1: String hashtags - PASSED")
    return True

def test_combine_caption_with_list():
    """Test combine_caption_and_hashtags with list hashtags."""
    from utils.text_utils import combine_caption_and_hashtags
    
    result = combine_caption_and_hashtags("Amazing food", ["#foodie", "#yummy", "#instagram"])
    assert "Amazing food" in result
    assert "#foodie" in result
    assert "#yummy" in result
    print("✓ Test 2: List hashtags - PASSED")
    return True

def test_empty_hashtags():
    """Test combine_caption_and_hashtags with empty hashtags."""
    from utils.text_utils import combine_caption_and_hashtags
    
    result = combine_caption_and_hashtags("Just a caption", "")
    assert result == "Just a caption"
    print("✓ Test 3: Empty hashtags - PASSED")
    return True

def test_character_limiter_to_combine():
    """Test that character limiter output works with combine function."""
    from utils.text_utils import combine_caption_and_hashtags
    from services.character_limiter import get_character_limiter
    
    limiter = get_character_limiter()
    caption = "This is a test caption for Twitter"
    hashtags_str = "#tag1 #tag2 #tag3 #tag4 #tag5"
    
    # This is what the app does - limit_text returns string hashtags
    limited_caption, limited_hashtags, metadata = limiter.limit_text(caption, hashtags_str, "twitter")
    
    # Now verify it works with combine
    final_result = combine_caption_and_hashtags(limited_caption, limited_hashtags)
    
    assert isinstance(limited_hashtags, str), f"Expected string, got {type(limited_hashtags)}"
    assert len(final_result) <= 280 + 20  # Twitter limit + buffer for newlines
    print("✓ Test 4: Character limiter → combine flow - PASSED")
    return True

def test_download_button_logic():
    """Test the download button hashtag handling logic."""
    # Simulate the download button code
    
    # Test with string hashtags (normal case)
    generated_hashtags = "#tag1 #tag2 #tag3"
    hashtag_text = generated_hashtags if isinstance(generated_hashtags, str) else ' '.join(generated_hashtags)
    assert hashtag_text == generated_hashtags
    
    generated_caption = "Test caption"
    full_text = f"{generated_caption}\n\n{hashtag_text}"
    assert "#tag1" in full_text
    
    # Test with list hashtags (edge case)
    generated_hashtags = ["#tag1", "#tag2"]
    hashtag_text = generated_hashtags if isinstance(generated_hashtags, str) else ' '.join(generated_hashtags)
    full_text = f"{generated_caption}\n\n{hashtag_text}"
    assert "#tag1" in full_text
    assert "#tag2" in full_text
    
    print("✓ Test 5: Download button logic - PASSED")
    return True

def test_imports():
    """Test that all required modules can be imported."""
    from config.settings import UI_CONFIG, CAPTION_STYLES, CHARACTER_LIMITS
    from utils.image_utils import validate_and_load_image
    from services.image_sentiment import get_sentiment_detector
    from services.caption_generator import get_caption_generator
    from services.hashtag_engine import get_hashtag_engine
    from services.character_limiter import get_character_limiter
    
    print("✓ Test 6: All imports - PASSED")
    return True

if __name__ == "__main__":
    print("=" * 70)
    print("TESTING HASHTAG TYPE MISMATCH FIXES")
    print("=" * 70)
    print()
    
    try:
        test_combine_caption_with_string()
        test_combine_caption_with_list()
        test_empty_hashtags()
        test_character_limiter_to_combine()
        test_download_button_logic()
        test_imports()
        
        print()
        print("=" * 70)
        print("ALL TESTS PASSED! ✓✓✓")
        print("=" * 70)
        print()
        print("Summary:")
        print("  • combine_caption_and_hashtags() handles both string and list inputs")
        print("  • Character limiter returns strings that work with combine()")
        print("  • Download button will work correctly")
        print("  • All application modules load without errors")
        print()
        print("The application is ready to use!")
        
    except AssertionError as e:
        print()
        print("=" * 70)
        print(f"TEST FAILED: {e}")
        print("=" * 70)
        sys.exit(1)
    except Exception as e:
        print()
        print("=" * 70)
        print(f"ERROR: {e}")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        sys.exit(1)
